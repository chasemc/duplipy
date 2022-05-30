import tarfile
from pathlib import Path
import subprocess
from duplipy.utils.logging_handler import log
import os

MICROMAMBA_HOOK = 'eval "$(./bin/micromamba shell hook -s posix)"'


class MM:
    def run_micromamba(
        self, mm_path="/Users/chase/Downloads/temp/micromamba", cl_args=None
    ):
        if mm_path.endswith("micromamba"):
            cl_list = [mm_path]
        if cl_args is None:
            log.info("No arguments to pass to micromamba")
        else:
            cl_list.extend(cl_args)
        subprocess.run(cl_list)

    def create_env(self):
        env = "export MAMBA_ROOT_PREFIX='/home/chase/Downloads/temp/micromamba'"
        subprocess.run(
            [
                'eval "$(/home/chase/Downloads/temp/micromamba shell hook -s posix)"',
                "micromamba",
                "create",
                "-n duplipy",
                "python=3.8",
            ],
            env=dict(
                os.environ,
                'MAMBA_ROOT_PREFIX':"/home/chase/Downloads/temp/micromamba",
                'MAMBA_EXE':"/home/chase/Downloads/temp/micromamba",
                'MAMBA_ROOT_PREFIX':"/home/chase/micromamba",
                'PATH':"/home/chase/micromamba/bin:$PATH",
            ),
            shell=True,
        )


a = MM()
a.create_env()


my_env = os.environ.copy()
my_env['MAMBA_ROOT_PREFIX'] ="/home/chase/Downloads/temp/micromamba"
my_env['MAMBA_EXE'] ="/home/chase/Downloads/temp/micromamba"
my_env['MAMBA_ROOT_PREFIX'] ="/home/chase/Downloads/temp"
my_env["PATH"] = "/home/chase/Downloads/temp:" + my_env["PATH"]

subprocess.run(
            " ".join([
                "micromamba",
                "create",
                "-n duplipy",
                "python=3.8",
            ]),
            env=my_env,
            shell=True,
        )

subprocess.run(
            " ".join([
                "micromamba",
                "clean --all --yes",
            ]),
            env=my_env,
            shell=True,
        )
