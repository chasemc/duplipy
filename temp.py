from rich import inspect
from duplipy.classes.duplipy import Duplipy

my_object = Duplipy(workdir='/Users/chase/Downloads/temp')


inspect(my_object)

my_object.easy_run()


my_object.install_r_package_with_renv(package="chasemc/demoapp")
