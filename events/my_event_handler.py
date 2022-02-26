from watchdog.events import FileSystemEventHandler

from CONSTANTS import PATH
from dataframes.dataframe_utils import update_df, add_to_df, remove_from_df


class my_event_handler(FileSystemEventHandler):
    def __init__(self, df, changed_df, directories_to_monitor):
        self.directories_to_monitor = directories_to_monitor
        self.df = df
        self.changed_df = changed_df

    def on_modified(self, event):
        print(event)
        # print(event.src_path, event.is_directory)

        if (not event.is_directory) and (event.src_path in self.df.index):
            update_df(self.df, self.changed_df, event.src_path)

    def on_created(self, event):
        print(event)

        if (not event.is_directory) and ( not (event.src_path in self.df.index)) :
            add_to_df(self.df, self.changed_df, event.src_path)
    def on_deleted(self, event):
        print(event)

        if (not event.is_directory) and (event.src_path in self.df.index):
            remove_from_df(self.df, self.changed_df, event.src_path)

    def on_moved(self, event):
        print(event)

        # if (not event.is_directory) and (event.src_path in self.df.index):
        #     remove_from_df(self.df, self.changed_df, event.src_path)
