from rich import inspect
from electricpy.classes.electricpy import electricpy

my_object = electricpy(workdir="/home/chase/Downloads/temp")

inspect(my_object)

my_object.easy_run()


my_object.install_r_package_with_renv(package="chasemc/demoapp")
