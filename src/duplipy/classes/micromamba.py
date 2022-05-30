import tarfile
from pathlib import Path
import subprocess
from duplipy.utils.logging_handler import log

MICROMAMBA_HOOK='eval "$(./bin/micromamba shell hook -s posix)"'


class MM():
    def run_micromamba(self, mm_path='/Users/chase/Downloads/temp/micromamba', cl_args=None):
        if mm_path.endswith("micromamba"):
        cl_list = [mm_path]
        if cl_args is None:
            log.info("No arguments to pass to micromamba")
        else:
            cl_list.extend(cl_args)
        subprocess.run(cl_list)
    def create_env(self):
        subprocess.run(['eval "$(/Users/chase/Downloads/temp/micromamba shell hook -s posix)"',
                        '/Users/chase/Downloads/temp/micromamba',
                        "create",
                        "-n xtensor_env",
                        "python=3.8"])
        


export MAMBA_ROOT_PREFIX=/Users/chase/Downloads/temp/micromamba
eval "$(/Users/chase/Downloads/temp/micromamba shell hook -s posix)"


