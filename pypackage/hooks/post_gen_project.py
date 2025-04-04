import os

REMOVE_PATHS = [
    '{% if not cookiecutter.use_docker %}docker-compose.yml{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
