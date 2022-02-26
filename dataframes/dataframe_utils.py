from time import ctime
import pandas as pd
import files.file_utils
from CONSTANTS import LAST_MODIFIED, HASH_256
from os.path import getmtime
pd.set_option("display.max_columns", None )


def update_df(df, changed_df, src_path):
    time_of_change = ctime(getmtime(src_path))
    df.loc[src_path, LAST_MODIFIED] = time_of_change

    new_hash = files.file_utils.find_hash_file_sha256(src_path)
    if new_hash != df.loc[src_path, HASH_256]:
        df.loc[src_path, HASH_256] = new_hash
        print(df.loc[src_path])
        # duplicate all the attributes except the last
        changed_df.loc[src_path] = df.loc[src_path]

    # print(f'Start df =  {df}')
    print(f'The changed df =  {changed_df}')


def add_to_df(df, changed_df, src_path):
    pass


def remove_from_df(df, changed_df, src_path):
    pass
