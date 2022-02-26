from hashlib import sha256
from os.path import isdir


def find_hash_file_sha256(files: str) -> str:
    """

    :param files: path to file
    :return: sha256 hash of the file
    """
    if isdir(files):
        return ""
    sha256_hash = sha256()
    with open(files, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    ret = str(sha256_hash.hexdigest())

    # print(ret)
    return ret

