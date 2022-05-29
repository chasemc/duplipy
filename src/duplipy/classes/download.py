import tarfile
from pathlib import Path
from duplipy.utils.downloader import download

class DownloadMicromamba:
    def __init__(self, workingdir):
        super().__init__()
        self.workingdir = workingdir
        self.download_dir = Path(workingdir, "downloads")
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.micromamba_path = None
    def download_mac(
        self,
        url="https://micro.mamba.pm/api/micromamba/osx-64/latest",
    ):
        download([url], self.download_dir)
        # extract out micromamba from the tar file
        with tarfile.open(Path(self.download_dir, "latest")) as tar:
            subdir_and_files = [
                tarinfo for tarinfo in tar.getmembers()
                if tarinfo.name.startswith("bin/micromamba")]
            member = subdir_and_files[0]
            member.name = "micromamba"
            tar.extract(member,path=self.download_dir)
        download_path = Path(self.download_dir, "micromamba")
        new_path = Path(self.workingdir, "micromamba")
        download_path.rename(new_path)
        self.micromamba_path = new_path
        Path(self.download_dir, "latest").unlink()
        
    
    