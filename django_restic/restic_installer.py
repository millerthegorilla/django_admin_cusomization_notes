import bz2
import json
import logging
import os
import hashlib
from shutil import which
from urllib.parse import urlparse

import requests

logger = logging.getLogger(__name__)


def restic_check() -> bool:
    try:
        if which("restic"):
            return True
        else:
            download_restic()
            return True
    except PermissionError as e:
        return False


def download_restic() -> None:
    github_json = json.loads(
        requests.get(
            "https://api.github.com/repos/restic/restic/releases/latest"
        ).content
    )

    download_url = ""
    checksum_url = ""
    file_found = False
    checksum_found = False
    for asset in github_json["assets"]:
        if "linux_amd64.bz2" in asset["name"]:
            download_url = asset["browser_download_url"]
            file_found = True
        if "SHA256SUMS" in asset["name"]:
            checksum_url = asset["browser_download_url"]
            checksum_found = True
        if file_found and checksum_found:
            break

    filename = os.path.basename(os.path.normpath(download_url))
    file = requests.get(download_url, allow_redirects=True).content
    hash = hashlib.sha256(file).hexdigest()
    checksums = requests.get(checksum_url, allow_redirects=True)
    checksum_found = False
    for line in checksums.iter_lines():
        if hash in line.decode('utf-8') and filename in line.decode('utf-8'):
            checksum_found = True
            break
    if not checksum_found or not 'objects.githubusercontent.com' in urlparse(checksums.url).netloc:
        raise LookupError("Checksum check failed!")

    program = bz2.decompress(file)

    try:
        path = "/usr/local/bin/restic"
        open(path, "wb").write(program)
        os.chmod(path, 0o755)
    except PermissionError as e:
        logger.ERROR("restic download failed - permissions error")
