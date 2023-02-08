from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class ChangeHandler(FileSystemEventHandler):
    """File system event handler that prints a message when a file or directory is modified.
    """

    def on_modified(self, event):
        """Called when a file or directory is modified.

        Parameters
        ----------
        event : FileSystemEvent
            Event object that contains information about the modification event.
        """
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))


def detect_changes(folder_path):
    """Monitors a folder for changes and prints a message when a file or directory is modified.

    Parameters
    ----------
    folder_path : str
        Path to the folder to be monitored.
    """
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
