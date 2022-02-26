import dotenv
from os.path import exists, abspath, split
from CONSTANTS import DIRECTORIES_TXT
from paths.path_utils import pathname_valid
from paths.path_utils import path_exists
from pathlib import Path

dotenv.load_dotenv()


def get_directories():
    if not exists(DIRECTORIES_TXT):
        raise (Exception(f'{DIRECTORIES_TXT} not found in the the path, please add it  to this directory'))

    dirs2 = []
    with open(DIRECTORIES_TXT, 'r') as f:
        dirs2 = f.readlines()

    dirs = []
    for directory in dirs2:
        dirs.append(directory[:-1:] if directory[-1] == '\n' else directory)

    for i, directory in enumerate(dirs):
        if not pathname_valid.pathname_valid(directory):
            raise (Exception(f'{directory} on line {i}  is not correctly writen'))

        if not path_exists.path_exists(directory):
            raise (Exception(f'{directory} on line {i} does not exist'))

    dirs_abs = []
    for directory in dirs:
        dirs_abs.append(abspath(directory))

    dirs_abs_set = set(dirs_abs)
    # for directory in dirs_abs:
    #     root = Path(directory)
    #     head, _ = split(root)
    #     if head:
    #         if head in dirs_abs_set:
    #             raise Exception(f'You cannot have {head} and {directory} because they nested')
    return dirs_abs
