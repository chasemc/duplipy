import tempfile
from pathlib import Path


class WorkingDir:
    def __init__(self, workdir=None, *args, **kwargs):
        """Path where all files will be created, miniconda downloaded/installed, etc

        Args:
            workdir (Path, optional): Path to empty directory. Defaults to None, which will use a temporary directory.
        """
        super().__init__(*args, **kwargs)
        if workdir == None:
            self.tempdir_path = tempfile.TemporaryDirectory()
            self.workdir = str(self.tempdir_path)
        else:
            self.workdir = str(Path(workdir))

    def clean_tempdir(self):
        self.tempdir_path = self.tempdir_path.cleanup()
