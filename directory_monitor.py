# directory_monitor.py
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")

def monitor_directory(path, duration=10):
    """
    Monitors the specified directory for changes for a given duration.
    
    Args:
        path (str): Path to the directory to monitor.
        duration (int): Duration in seconds to monitor the directory.
    """
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        time.sleep(duration)
    finally:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    directory_to_monitor = "./monitor_folder"
    print(f"Monitoring directory: {directory_to_monitor} for {10} seconds...")
    monitor_directory(directory_to_monitor)
    print("Monitoring ended.")
