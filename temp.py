from rich import inspect
from duplipy.classes.duplipy import Duplipy

my_object = Duplipy(
    workdir="/Users/chase/Downloads/test", user_app_path="chasemc/demoapp"
)
inspect(my_object)

my_object.easy_run()
