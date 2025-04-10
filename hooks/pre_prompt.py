import os
import shutil
import subprocess
from pathlib import Path


root_path = Path(os.path.dirname(os.path.abspath(__file__))).parent
base_path = root_path / "base"
source_dirs = [
    "hooks",
    "{{ cookiecutter.repo_name }}",
]

dest_folders = ['py', 'pypackage', 'drf', 'drf_package']


def merge_directories(src, dst):
    """
    Recursively merge source directory into destination directory.
    If a file exists in both places, the source file will override the destination file.
    If a directory exists in both places, their contents will be merged.
    """
    # Make sure destination directory exists
    os.makedirs(dst, exist_ok=True)

    # Iterate through all items in source directory
    for item in src.iterdir():
        dest_item = dst / item.name

        # If item is a directory, recursively merge it
        if item.is_dir():
            merge_directories(item, dest_item)
        # If item is a file, copy it (overwriting if exists)
        else:
            if not dest_item.exists():
                shutil.copy2(item, dest_item)


def copy_and_merge_directories():
    # Define source and destination paths relative to the script location
    # List contents of the directories
    for source_path in source_dirs:
        # Check if source directory exists
        source_dir = base_path / source_path
        if not source_dir.exists():
            continue

        for dest in dest_folders:
            dest_dir = root_path / dest / source_path

            # Create destination directory if it doesn't exist
            os.makedirs(dest_dir, exist_ok=True)

            # Merge the directories
            merge_directories(source_dir, dest_dir)

copy_and_merge_directories()
