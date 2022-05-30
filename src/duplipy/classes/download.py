import tarfile
from pathlib import Path
from sys import platform
from duplipy.utils.downloader import download
from duplipy.utils.md5_file import md5_file
from duplipy.utils.logging_handler import log

MAC_VERSION="0.23.3"
MAC_MD5="5e3ccd398a0a0d3c043c974f03e86ad3"
   
MICROMAMBA_BASE_URL = 'https://micro.mamba.pm/api/micromamba'
MAMBA_PLATFORM = { "darwin": 'osx', "linux": 'linux', "win32": 'win' }[platform]
if not MAMBA_PLATFORM:
  raise ValueError(f"Platform {platform} not supported")
MICROMAMBA_PLATFORM_URL = Path(MICROMAMBA_BASE_URL,f"{MAMBA_PLATFORM}-64")
MICROMAMBA_URL = Path(MICROMAMBA_PLATFORM_URL,MAC_VERSION)
   
class DownloadMicromamba:
    def __init__(self, workingdir):
        super().__init__()
        self.workingdir = workingdir
        self.download_dir = Path(workingdir, "downloads")
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.micromamba_path = None
        self.url = Path(MAC_VERSION)
        self.download_filepath = Path(self.download_dir, self.url.stem)
    def _check_hash(self):
        calculated_hash = md5_file(self.download_filepath)
        if calculated_hash == MAC_MD5:
            log.info(f"MD5 check passed: {self.url.stem}")
        else:
            raise ValueError(f"MD5 check failed: {self.url.stem}")
    def _extract_from_tar(self, compression= "r:bz2"):
        with tarfile.open(self.download_filepath, compression) as tar:
            subdir_and_files = [
                tarinfo for tarinfo in tar.getmembers()
                if tarinfo.name.startswith("bin/micromamba")]
            member = subdir_and_files[0]
            member.name = "micromamba"
            tar.extract(member,path=self.download_dir)
    def _stage_micromamba(self):
            download_path = Path(self.download_dir, "micromamba")
            new_path = Path(self.workingdir, "micromamba")
            download_path.rename(new_path)
            self.micromamba_path = new_path
    def _cleanup(self):
        Path(self.download_dir, "latest").unlink()  
    def download_mac(
        self,
        url=MAC_VERSION,
    ):
        download([url], self.download_dir)
        #self._check_hash()
        #self._extract_from_tar(compression= "r:bz2")
        #self._stage_micromamba()
        #self._cleanup()
    



