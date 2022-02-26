from os import walk, path
from time import ctime
import pandas as pd
from CONSTANTS import SIMPLE_COLUMNS, SIMPLE_DF_INDEX_NAME
from files.file_utils import find_hash_file_sha256


def walklevel(some_dir='./', max_level=1) -> pd.DataFrame:
    num_sep = some_dir.count(path.sep)  # start path length
    curr_info = []
    for root, dirs, files in walk(some_dir):
        depth = root.count(path.sep) - num_sep
        if depth <= max_level:
            for file in files:
                if file:
                    file_path = path.join(root, file)
                    curr_info.append(
                        [file_path, file, 'file', ctime(path.getmtime(file_path)), find_hash_file_sha256(file_path)])
    # print(curr_info)
    df = pd.DataFrame(curr_info, columns=SIMPLE_COLUMNS)
    df = df.set_index(SIMPLE_DF_INDEX_NAME)
    return df


def init_monitor_df(df: pd.DataFrame, directories_to_monitor: []) -> pd.DataFrame:
    df.set_index(SIMPLE_DF_INDEX_NAME, inplace=True)
    for i, directory in enumerate(directories_to_monitor):
        new_files = walklevel(some_dir=directory)
        new_files.sort_index(inplace=True)

        if not df.empty:
            indexes_1 = new_files.index.to_list()
            indexes_2 = df.index.to_list()
            # print(indexes_1)
            # print(indexes_2)
            res = list(set(indexes_1).intersection(indexes_2))
            # print(res)
            if res:
                raise Exception(f' There are overlapping files on {res}')

        df = df.append(new_files)

    df.sort_index(inplace=True)
    return df
