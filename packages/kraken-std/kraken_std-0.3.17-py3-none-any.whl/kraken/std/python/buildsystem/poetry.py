""" Implements Poetry as a build system for kraken-std. """

from __future__ import annotations

import contextlib
import logging
import os
import shutil
import subprocess as sp
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import tomli
import tomli_w
from kraken.core.util.fs import atomic_file_swap
from kraken.core.util.helpers import NotSet
from kraken.core.util.path import is_relative_to
from nr.python.environment.virtualenv import get_current_venv

from kraken.std.python.settings import PythonSettings

from . import ManagedEnvironment, PythonBuildSystem

logger = logging.getLogger(__name__)


class PoetryPythonBuildSystem(PythonBuildSystem):
    name = "Poetry"

    def __init__(self, project_directory: Path) -> None:
        self.project_directory = project_directory

    def supports_managed_environments(self) -> bool:
        return True

    def get_managed_environment(self) -> ManagedEnvironment:
        return PoetryManagedEnvironment(self.project_directory)

    def build(self, output_directory: Path, as_version: str | None = None) -> list[Path]:
        if as_version is not None:
            # TODO (@NiklasRosenstein): We should find a way to revert the changes to the worktree
            #       that this command does.
            command = ["poetry", "version", as_version]
            logger.info("%s", command)
            sp.check_call(command, cwd=self.project_directory)

        # Poetry does not allow configuring the output folder, so it's always going to be "dist/".
        # We remove the contents of that folder to make sure we know what was produced.
        dist_dir = self.project_directory / "dist"
        if dist_dir.exists():
            shutil.rmtree(dist_dir)

        command = ["poetry", "build"]
        logger.info("%s", command)
        sp.check_call(command, cwd=self.project_directory)
        src_files = list(dist_dir.iterdir())
        dst_files = [output_directory / path.name for path in src_files]
        for src, dst in zip(src_files, dst_files):
            shutil.move(str(src), dst)

        # Unless the output directory is a subdirectory of the dist_dir, we remove the dist dir again.
        if not is_relative_to(output_directory, dist_dir):
            shutil.rmtree(dist_dir)

        return dst_files


class PoetryManagedEnvironment(ManagedEnvironment):
    def __init__(self, project_directory: Path) -> None:
        self.project_directory = project_directory
        self._env_path: Path | None | NotSet = NotSet.Value

    def _get_current_poetry_environment_path(self) -> Path | None:
        """Uses `poetry env info -p`. This will not work if Poetry has to fall back to a compatible Python
        version if the version that Poetry is installed into is not compatible."""

        # Ensure we de-activate any environment that might be active when Kraken is invoked. Otherwise,
        # Poetry would fall back to that environment.
        environ = os.environ.copy()
        venv = get_current_venv(environ)
        if venv:
            venv.deactivate(environ)

        command = ["poetry", "env", "info", "-p"]
        try:
            response = sp.check_output(command, cwd=self.project_directory, env=environ).decode().strip()
        except sp.CalledProcessError as exc:
            if exc.returncode != 1:
                raise
            return None
        else:
            return Path(response)

    def _get_all_poetry_known_environment_paths(self) -> list[Path]:
        """Uses `poetry env list --full-path` to get the path to all relevant virtual environments that are known
        to Poetry for the project. We fall back to this method if `poetry env info -p` fails us."""

        command = ["poetry", "env", "list", "--full-path"]
        try:
            response = sp.check_output(command, cwd=self.project_directory).decode().strip().splitlines()
        except sp.CalledProcessError as exc:
            if exc.returncode != 1:
                raise
            return []
        else:
            return [Path(line) for line in response if line]

    def _get_poetry_environment_path(self) -> Path | None:
        # Run the two Poetry commands we need to run in parallel to improve load times.
        with ThreadPoolExecutor() as executor:
            venv_path_future = executor.submit(self._get_current_poetry_environment_path)
            known_venvs_future = executor.submit(self._get_all_poetry_known_environment_paths)
            venv_path = venv_path_future.result()
            if venv_path is not None:
                return venv_path
            known_venvs = known_venvs_future.result()
            if known_venvs:
                if len(known_venvs) > 1:
                    logger.warning(
                        "This project has multiple Poetry environments. Picking the first one (%s)", known_venvs[0]
                    )
                return known_venvs[0]
            return None

    # ManagedEnvironment

    def exists(self) -> bool:
        try:
            self.get_path()
            return True
        except RuntimeError:
            return False

    def get_path(self) -> Path:
        if self._env_path is NotSet.Value:
            self._env_path = self._get_poetry_environment_path()
        if self._env_path is None:
            raise RuntimeError("managed environment does not exist")
        return self._env_path

    def install(self, settings: PythonSettings) -> None:

        # Ensure that `poetry.toml` is up to date with the credentials.
        poetry_toml = self.project_directory / "poetry.toml"
        poetry_conf = tomli.loads(poetry_toml.read_text()) if poetry_toml.exists() else {}

        # Ensure that the source is configured in `pyproject.toml`.
        # TODO (@NiklasRosenstein): Maybe we should permanently sync the source configuration into the
        #       pyproject.toml instead of just temporarily?
        pyproject_toml = self.project_directory / "pyproject.toml"
        pyproject_conf = tomli.loads(pyproject_toml.read_text())
        sources_conf = pyproject_conf.setdefault("tool", {}).setdefault("poetry", {}).setdefault("source", [])

        for index in settings.package_indexes.values():
            if index.is_package_source and index.credentials:
                poetry_conf.setdefault("http-basic", {})[index.alias] = {
                    "username": index.credentials[0],
                    "password": index.credentials[1],
                }

                source_config = {
                    "name": index.alias,
                    "url": index.index_url,
                    "secondary": True,
                }

                # Find the source with the same name and update it, or create a new one.
                source = next((x for x in sources_conf if x["name"] == index.alias), None)
                if source is None:
                    sources_conf.append(source_config)
                else:
                    source.update(source_config)

        with contextlib.ExitStack() as exit_stack:
            fp = exit_stack.enter_context(atomic_file_swap(poetry_toml, "wb", always_revert=True))
            tomli_w.dump(poetry_conf, fp)
            fp.close()

            fp = exit_stack.enter_context(atomic_file_swap(pyproject_toml, "wb", always_revert=True))
            tomli_w.dump(pyproject_conf, fp)
            fp.close()

            command = ["poetry", "install", "--no-interaction"]
            logger.info("%s", command)
            sp.check_call(command, cwd=self.project_directory)
