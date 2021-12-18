import tempfile


class WorkingDir:
    def __init__(self, workdir=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if workdir == None:
            self.tempdir_path = tempfile.TemporaryDirectory()
            self.workdir = self.tempdir_path
        else:
            self.workdir = workdir

    def clean_tempdir(self):
        self.tempdir_path = self.tempdir_path.cleanup()
