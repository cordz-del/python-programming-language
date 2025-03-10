# test_file_renamer.py
import os
import tempfile
import shutil
from file_renamer import rename_files_in_directory

def test_rename_files_in_directory():
    temp_dir = tempfile.mkdtemp()
    try:
        # Create dummy files
        filenames = ["file1_old.txt", "file2_old.txt", "file3.txt"]
        for name in filenames:
            open(os.path.join(temp_dir, name), "w").close()
        
        renamed = rename_files_in_directory(temp_dir, r"_old", "")
        expected = ["file1.txt", "file2.txt"]
        assert set(renamed) == set(expected)
        final_files = os.listdir(temp_dir)
        assert "file1.txt" in final_files and "file2.txt" in final_files and "file3.txt" in final_files
        print("test_rename_files_in_directory passed.")
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    test_rename_files_in_directory()
