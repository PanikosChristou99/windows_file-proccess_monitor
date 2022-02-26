import time
import pandas as pd
from watchdog.observers import Observer
from CONSTANTS import SIMPLE_COLUMNS, SIMPLE_DF_INDEX_NAME
from directories.directory_utils import get_directories
from directories.walk_dirs import init_monitor_df
from events.my_event_handler import my_event_handler

pd.set_option("display.max_columns", None, 'display.max_colwidth', 18)


def main():
    # Get directories from .txt and check em
    directories_to_monitor = get_directories()

    # init df
    df = pd.DataFrame([], columns=SIMPLE_COLUMNS)
    df = init_monitor_df(df, directories_to_monitor)

    if df.empty:
        raise Exception('No files to monitor')
    print(df)

    # init my event handler
    changed_df = pd.DataFrame([], columns=SIMPLE_COLUMNS).set_index(SIMPLE_DF_INDEX_NAME)
    event_handler = my_event_handler(df, changed_df, directories_to_monitor)

    observers = []

    for directory in directories_to_monitor:
        observer = Observer()
        print(f'observing {directory}')
        observer.schedule(event_handler, directory)
        observers.append(observer)

    for observer in observers:
        observer.start()

    start_time = time.time()
    try:
        while True:
            time.sleep(10)
            print(f'been running for {time.time() - start_time} seconds')
    finally:
        for observer in observers:
            observer.stop()
            observer.join()
        print('Goodbye')


if __name__ == '__main__':
    main()
