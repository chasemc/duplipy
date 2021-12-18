# python dependencies
import subprocess
from sys import platform
from typing import List

# internal dependencies
from electricpy.utils.logging_handler import log


def check_os(
    os: str = platform, supported_os: List = ["linux", "linux2", "darwin", "win32"]
):
    if os in supported_os:
        response = os
    else:
        message = "".join(
            [
                "Operating system found: '",
                str(os),
                "'. Must be one of: ",
                ", ".join(supported_os),
            ]
        )
        log.error(message)
        raise ValueError(message)

    log.info("".join(["Operating system: ", response]))
    return response


def run_command(command: List = None, shell=False):
    log.info(" ".join(command))
    with subprocess.Popen(args=command, shell=shell, stdout=subprocess.PIPE) as proc:
        log.info(proc.stdout.read().decode("utf-8"))


# def create_remotes_install_function():


# check_for_remoted
# """
# inherits(getFromNamespace('install_github', ns = 'remotes'),'function')
# """
