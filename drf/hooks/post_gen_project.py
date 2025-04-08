import os
import shutil
import subprocess
from pathlib import Path

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def cleanup_files():
    """Remove files based on cookiecutter options."""
    # Remove websocket-related files if not using websockets
    if "{{ cookiecutter.use_websocket }}" == "false":
        print(INFO + "Removing websocket-related files..." + TERMINATOR)
        paths_to_remove = [
            Path("{{cookiecutter.project_slug}}", "chat"),
            Path("{{cookiecutter.project_slug}}", "config", "routing.py"),
        ]

        for path in paths_to_remove:
            if path.exists():
                print(INFO + f"Removing {path}" + TERMINATOR)
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()

    # Remove Google login related files if not using Google login
    if "{{ cookiecutter.google_login }}" == "false":
        print(INFO + "Removing Google login files..." + TERMINATOR)
        google_login_view = Path("{{cookiecutter.project_slug}}", "accounts", "views", "google_login_view.py")
        if google_login_view.exists():
            google_login_view.unlink()

    # Remove Celery files if not using Celery
    if "{{ cookiecutter.use_celery }}" == "false":
        print(INFO + "Removing Celery files..." + TERMINATOR)
        celery_app_path = Path("{{cookiecutter.project_slug}}", "config", "celery_app.py")
        if celery_app_path.exists():
            celery_app_path.unlink()

    # Copy .env.TEMPLATE to .env
    template_path = Path(".env.TEMPLATE")
    env_path = Path(".env")
    if template_path.exists():
        print(INFO + "Copying .env.TEMPLATE to .env" + TERMINATOR)
        shutil.copy(template_path, env_path)

    # Initialize git
    print(INFO + "Initializing git repository" + TERMINATOR)
    subprocess.run(["git", "init"], check=True)


if __name__ == "__main__":
    print(INFO + "Starting cleanup process..." + TERMINATOR)
    cleanup_files()
    print(SUCCESS + "Cleanup completed successfully!" + TERMINATOR)
