# WARNING

This is still very much a work in progress and nothing can be assumed stable in any way

Temp notes:

Two types of created installer, based on whether it contains:

1. All dependencies (conda, R, R packages, Shiny app, etc)
2. Strict instructions for dependency install


## Overview


Create standalone, installable R Shiny apps using Electron

## Installation

You can also install the in-development version with::

    pip install https://github.com/chasemc/duplipy/archive/main.zip


## Documentation

https://chasemc.github.io/duplipy/

To use the project:

```{python}
from duplipy.classes.duplipy import Duplipy

my_object = Duplipy(
    workdir="/Users/chase/Downloads/test", user_app_path="chasemc/demoapp"
)
inspect(my_object)

my_object.easy_run()
```

Note: Electron part still hasn't been added, currently this stops after the conda/renv file creation step

