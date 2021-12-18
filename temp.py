from rich import inspect # not needed to run, ony importede here to pretty-print results
import os
from pathlib import Path

from electricpy.classes.electricpy import electricpy
my_object = electricpy(workdir="/home/chase/Downloads/temp")


my_object.download_miniconda3()
my_object.install_miniconda()


my_object.conda_create_env("eshine")
my_object.install_r(env_name="eshine", r_version="4.0.0")
my_object.install_r_package(env_name="eshine", r_package_name="renv")
my_object.renv_init(env_name="eshine")
my_object.install_r_package_With_renv(env_name="eshine", package="chasemc/demoapp")
## Install all dependencies on user-side
my_object.export_env("eshine")
my_object.renv_snap(env_name="eshine")
