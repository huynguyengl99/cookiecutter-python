import os
import subprocess

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def init():
    REMOVE_PATHS = [
{%- if not cookiecutter.use_websocket %}
        'sandbox/config/routing.py',
{% endif %}
    ]

    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            os.unlink(path) if os.path.isfile(path) else os.rmdir(path)

    subprocess.run(["git", "init"], check=True)


if __name__ == "__main__":
    print(INFO + "Starting post gen project process..." + TERMINATOR)
    init()
    print(SUCCESS + "Process completed successfully!" + TERMINATOR)
