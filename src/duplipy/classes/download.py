import tarfile
from pathlib import Path
import platform
from duplipy.classes.operating_system import OperatingSystem
from duplipy.utils.downloader import download
from duplipy.utils.md5_file import md5_file
from duplipy.utils.logging_handler import log
import requests
import json
from duplipy.utils.issues import create_url


MICROMABA_VERSION = "0.23.0"
ANACONDA_URL = (
    f"https://api.anaconda.org/release/conda-forge/micromamba/{MICROMABA_VERSION}"
)


class DownloadMicromamba(OperatingSystem):
    def __init__(self, workingdir):
        super().__init__()
        self.workingdir = workingdir
        self.download_dir = Path(workingdir, "downloads")
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.micromamba_path = None
        self.expected_md5 = None
        self.download_url = None
        self.download_filepath = None

    def _get_url(self):
        j = requests.get(ANACONDA_URL).json()
        matching_system = [
            i
            for i in j["distributions"]
            if i["attrs"]["arch"] == self.this_machine
            and i["attrs"]["platform"] == self.this_operating_system
        ]
        if len(matching_system) > 1:
            collect_attrs = "; ".join(
                [
                    f"{i['attrs']['arch']},{i['attrs']['platform']},{i['attrs']['target-triplet']}"
                    for i in matching_system
                ]
            )
            raise ValueError(
                f"""
                Found {len(matching_system)} matching download urls.
                Please open an issue using the following link:
                {create_url('Multiple matching systems', 'bug', collect_attrs)}
                """
            )
        elif not len(matching_system) == 1:
            raise ValueError(
                f"Found {len(matching_system)} matching download urls, expected 1: {matching_system}"
            )
        self.expected_md5 = matching_system[0]["md5"]  # TODO:should hardcode
        self.download_url = f"https:{matching_system[0]['download_url']}"
        self.download_filepath = Path(self.download_dir, Path(self.download_url).name)

    def _check_hash(self):
        calculated_hash = md5_file(self.download_filepath)
        if calculated_hash == self.expected_md5:
            log.info(f"MD5 check passed: {Path(self.download_url).name}")
        else:
            raise ValueError(f"MD5 check failed: {Path(self.download_url).name}")

    def _extract_from_tar(self, compression="r:bz2"):
        with tarfile.open(self.download_filepath, compression) as tar:
            subdir_and_files = [
                tarinfo
                for tarinfo in tar.getmembers()
                if tarinfo.name.startswith("bin/micromamba")
            ]
            member = subdir_and_files[0]
            member.name = "micromamba"
            tar.extract(member, path=self.download_dir)

    def _stage_micromamba(self):
        download_path = Path(self.download_dir, "micromamba")
        new_path = Path(self.workingdir, "micromamba")
        download_path.rename(new_path)
        self.micromamba_path = new_path

    def _cleanup(self):
        self.download_filepath.unlink()

    def download(
        self,
    ):
        self._get_url()
        url = str(self.download_url)
        download([url], self.download_dir)
        self._check_hash()
        self._extract_from_tar(compression="r:bz2")
        self._stage_micromamba()
        self._cleanup()
