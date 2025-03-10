# file_renamer.py
import os
import re

def rename_files_in_directory(directory, pattern, replacement):
    """
    Renames files in the given directory by applying a regex pattern and replacement.
    
    Args:
        directory (str): Path to the directory containing files.
        pattern (str): Regex pattern to search for in file names.
        replacement (str): Replacement string for matched patterns.
    
    Returns:
        List[str]: List of new file names.
    """
    renamed_files = []
    for filename in os.listdir(directory):
        new_filename = re.sub(pattern, replacement, filename)
        if new_filename != filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            renamed_files.append(new_filename)
    return renamed_files

if __name__ == "__main__":
    # Example usage
    directory = "./test_files"
    pattern = r"_old"
    replacement = ""
    print("Renamed files:", rename_files_in_directory(directory, pattern, replacement))
