from pathlib import Path
from shlex import quote

from packaging import version

from duplipy.classes.conda import CondaEnvs
from duplipy.utils.logging_handler import log


class Duplipy(CondaEnvs):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renv_project_directory = self.workdir

    def _is_workdir_empty(self):
        if any(Path(self.workdir).iterdir()):
            return False
        else:
            log.info("Provided working directory is empty")
            return True

    def _check_for_conda_dir(self):
        return Path(self.conda_topdir).is_file()

    def _check_for_conda_exec(self):
        return Path(self.get_conda_executable()).is_file()

    def _attempt_reuse(self):
        # if provided workdir isn't empty, check if it contains conda...
        if self._is_workdir_empty():
            if self._check_for_conda_exec():
                self.conda_executable = str(Path(self.get_conda_executable()))
                return True
            else:
                return False
        else:
            return False

    def easy_run(self):
        if not self._attempt_reuse():
            log.info("Installing miniconda")
            self.download_miniconda3()
            self.install_miniconda()
        self.conda_create_env(env_name=self.build_environment)
        self.install_r(r_version="4.0.0")
        self.install_r_package(r_package_name="renv")
        self.renv_init()
        self.install_r_package_with_renv(package="chasemc/demoapp")
        self.export_env()
        self.renv_snap()
