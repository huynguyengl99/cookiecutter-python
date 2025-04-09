import os
import shutil
import subprocess
from pathlib import Path

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def init():
    subprocess.run(["git", "init"], check=True)


if __name__ == "__main__":
    print(INFO + "Starting post gen project process..." + TERMINATOR)
    init()
    print(SUCCESS + "Process completed successfully!" + TERMINATOR)
