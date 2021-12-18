# python dependencies

import datetime
import os
import platform
from pathlib import Path
from shlex import quote
from typing import List

from packaging import version
# external dependencies
from rich import inspect
from rich import print

# internal dependencies
from electricpy.classes.operating_system import OperatingSystem
from electricpy.classes.paths_setup import WorkingDir
from electricpy.utils.downloader import download
from electricpy.utils.run_command import run_command


class Conda(WorkingDir, OperatingSystem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conda_installer_script_path = None
        self.conda_topdir = None
        self.conda_executable = None

    def reload_dir(self):
        self.workdir


    def download_miniconda3(
        self,
        semver="latest",
    ):
        if self.this_operating_system in ["linux", "linux2"]:
            miniconda_os = "Linux"
        elif self.this_operating_system == "darwin":
            miniconda_os = "MacOSX"
        elif self.this_operating_system == "win32":
            miniconda_os = "Windows"

        if semver == "latest":
            semver = "latest"
        else:
            semver = version.parse(semver)
            semver = ".".join(
                [
                    str(semver.major),
                    str(semver.minor),
                    str(semver.micro),
                ]
            )

        miniconda_filename = "".join(
            [
                "Miniconda3-",
                semver,
                "-",
                miniconda_os,
                "-",
                str(platform.machine()),
                ".sh",
            ]
        )

        miniconda_url = "".join(
            [
                "https://repo.anaconda.com/miniconda/",
                miniconda_filename,
            ]
        )
        download([miniconda_url], self.workdir)
        self.conda_installer_script_path = str(Path(self.workdir, miniconda_filename))
        os.chmod(str(self.conda_installer_script_path), 0o755)

    def install_miniconda(self):

        self.conda_topdir = Path(self.workdir, "conda_topdir")
        if not Path(self.conda_topdir).exists():
            os.makedirs(self.conda_topdir)

        # p = run_command(
        # [
        # quote(str(self.conda_installer_script_path)),
        # "-bup",
        # quote(str(self.conda_topdir)),
        # ]
        # )

        p = run_command(
            [
                quote(str(self.conda_installer_script_path)),
                "-bup",
                str(self.conda_topdir),
            ]
        )

        self.conda_executable = self.get_conda_executable()
        print(inspect(self))

    def get_conda_executable(self):
        """Get the path to ~/bin/conda for an environment
        Returns:
            str: Path as string
        """
        return str(Path(self.conda_topdir, "bin", "conda"))

    def conda_install(self, env_name, package, repo):
        conda_exec = Path(self.conda_topdir, "bin", "conda")
        run_command(
            [
                quote(str(conda_exec)),
                "install",
                "--name",
                env_name,
                "--channel",
                repo,
                package,
                "-y",
            ]
        )

    def install_r_package(
        self,
        env_name,
        r_package_name,
        r_package_repo: str = "https://cran.r-project.org",
    ):
        rscript_path = str(
            Path(self.conda_topdir, "envs", env_name, "lib", "R", "bin", "Rscript")
        )

        r_lib = str(Path(self.conda_topdir, "envs", env_name, "lib", "R", "library"))

        r_script = "".join(
            [
                "install.packages(",
                "'",
                r_package_name,
                "'",
                ",",
                "repos=",
                "'",
                r_package_repo,
                "'",
                ",",
                "lib=",
                "'",
                r_lib,
                "'",
                ")",
            ]
        )
        command_list = [rscript_path, "-e", r_script]
        self.environments[env_name].run_command_with_conda_env(
            conda_executable=self.conda_executable, command=command_list
        )

    def install_r_package_with_renv(
        self,
        env_name,
        package="chasemc/demoapp",
        dependencies_repo="https://cran.r-project.org",
    ):

        r_lib = str(Path(self.conda_topdir, "envs", env_name, "lib", "R", "library"))

        remotes_install = "".join(
            [
                "renv::install(",
                f"'{package}'",
                ", ",
                f"repos = '{dependencies_repo}'",
                ", ",
                f"lib = '{r_lib}'",
                ", ",
                f"force = FALSE",
                ", ",
                f"project= '{self.renv_project_directory}'",
                ")",
            ]
        )
        remotes_install = quote(remotes_install)
        rscript_path = str(
            Path(self.conda_topdir, "envs", env_name, "lib", "R", "bin", "Rscript")
        )
        command_list = [rscript_path, "-e", remotes_install]

        self.environments[env_name].run_command_with_conda_env(
            conda_executable=self.conda_executable, command=command_list
        )

    def renv_init(self, env_name):
        rscript_path = str(
            Path(self.conda_topdir, "envs", env_name, "lib", "R", "bin", "Rscript")
        )
        r_lib = str(Path(self.conda_topdir, "envs", env_name, "lib", "R", "library"))
        r_command = f'renv::consent(provided=TRUE); renv::init(project ="{self.renv_project_directory}",settings=list(external.libraries="{r_lib}",use.cache =FALSE,vcs.ignore.library=TRUE,package.dependency.fields=c("Imports","Depends","LinkingTo")),bare=TRUE,restart=FALSE)'
        command_list = [
            rscript_path,
            "-e",
            r_command,
        ]
        self.environments[env_name].run_command_with_conda_env(
            conda_executable=self.conda_executable, command=command_list
        )

    def renv_snap(self, env_name):
        rscript_path = str(
            Path(self.conda_topdir, "envs", env_name, "lib", "R", "bin", "Rscript")
        )
        r_lib = str(Path(self.conda_topdir, "envs", env_name, "lib", "R", "library"))
        r_command = f'renv::snapshot(project="{self.renv_project_directory}",library="{r_lib}",lockfile="{str(Path(self.workdir,"renv_dependencies.lock"))}",packages=NULL,type="all",prompt=FALSE,force=FALSE)'
        command_list = [
            rscript_path,
            "-e",
            r_command,
        ]
        self.environments[env_name].run_command_with_conda_env(
            conda_executable=self.conda_executable, command=command_list
        )

    def export_env(self, env_name):
        outpath = Path(self.workdir, "conda_dependencies.yml")
        command = "".join(
            [
                str(self.conda_executable),
                " ",
                "env",
                " ",
                "export",
                " ",
                "-n",
                " ",
                env_name,
                " ",
                ">",
                " ",
                f"{str(outpath)}",
            ]
        )
        run_command(command=[command], shell=True)
        # remove "prefix:"" line from file
        lines = []
        with open(outpath, "r") as con:
            lines = con.readlines()
        with open(outpath, "w") as con:
            for line in lines:
                if not line.startswith("prefix:"):
                    con.write(line)


class CondaEnvs(Conda):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.environments = {}

    def conda_create_env(self, env_name):
        run_command([str(self.conda_executable), "create", "-n", env_name, "-y"])
        self.environments[env_name] = CondaEnvironment(env_name=env_name)

    def environment_path(self, env_name):
        return Path(self.conda_topdir, "envs", env_name)


class CondaEnvironment:
    def __init__(
        self,
        env_name: str,
    ):
        self.env_name = env_name
        self.env_history = []

    def run_command_with_conda_env(self, conda_executable, command: List):
        conda_exec = conda_executable
        command_list = [conda_exec, "run", "-n", self.env_name, "--live-stream"]
        command_list.extend(command)
        run_command(command_list)

        str_for_history = " ".join(command_list)

        str_for_history = "".join(
            [datetime.datetime.utcnow().isoformat(), "\t", str_for_history]
        )
        print(str_for_history)
        self.env_history.append(str_for_history)
