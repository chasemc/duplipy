from pathlib import Path
from shlex import quote

from packaging import version

from electricpie.classes.conda import CondaEnvs
from electricpie.utils.run_command import run_command


class Electricpie(CondaEnvs):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renv_project_directory = self.workdir

    def install_r(self, env_name, r_version):
        semver = version.parse(r_version)
        semver = ".".join(
            [
                str(semver.major),
                str(semver.minor),
                str(semver.micro),
            ]
        )
        r_and_semver = "".join([str("r-base="), semver])
        self.conda_install(env_name=env_name, package=r_and_semver, repo="conda-forge")
