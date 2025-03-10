# test_directory_monitor.py
import os
import time
import tempfile
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class TestEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.modified_files = []
    def on_modified(self, event):
        if not event.is_directory:
            self.modified_files.append(event.src_path)

def test_monitor_directory():
    temp_dir = tempfile.mkdtemp()
    handler = TestEventHandler()
    observer = Observer()
    observer.schedule(handler, temp_dir, recursive=False)
    observer.start()
    
    # Create and modify a file to trigger events
    test_file = os.path.join(temp_dir, "test.txt")
    with open(test_file, "w") as f:
        f.write("Initial content")
    
    time.sleep(1)
    
    with open(test_file, "a") as f:
        f.write(" More content")
    
    time.sleep(1)
    
    observer.stop()
    observer.join()
    
    assert test_file in handler.modified_files, "File modification was not detected."
    print("test_monitor_directory passed.")
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    test_monitor_directory()
