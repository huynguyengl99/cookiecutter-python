# {{ cookiecutter.project_name }}

## 1. Introduction

{{ cookiecutter.description }}

## 2. Stack & Framework
- [Django](https://www.djangoproject.com/) - Batteries-included Python web framework.
- [PostgreSQL](https://www.postgresql.org/) - Well-know open source database system.

## 3. Dev tools (must install for local development)
- [UV](https://docs.astral.sh/uv/): python version & packages management.
- [Docker](https://www.docker.com/products/docker-desktop/): docker app for launching services like db, redis, e.t.c.

## 4. Getting started
### Environment & dependencies setup (UV installed)
- Create virtual env for easier maintain:
```bash
uv venv
```
- Sourcing the .venv:
```bash
source .venv/bin/activate
```
- Install all dependencies:
```bash
uv sync
```

### Run backend
- Edit the environment variables in [.env](.env) file.
- Start docker:
```bash
docker compose up --detach
```
- Run migrations
```bash
scripts/manage.sh migrate
```
- Create superuser to access to admin page
```bash
scripts/manage.sh createsuperuser
```
- Start server
```bash
scripts/manage.sh runserver 8000
```
- Visit API playground and API documentation at:
  - API playground(Swagger): http://localhost:8000/api/cms-schema/swg/.
  - API documentation: http://localhost:8000/api/cms-schema/redoc/
- (Optional) To set up pre-commit hook (to automatically code formatting and dependencies checking before commit) run:
```bash
pre-commit install
```
  (more info below)


## 5. Utilities
### Useful command:
- [scripts/manage.sh](scripts/manage.sh): aliases for `python {{ cookiecutter.project_slug }}/manage.py` or `django-admin`, can config env later.
- Usually use:
  - `scripts/manage.sh runserver 8000`: Run local server.
  - `scripts/manage.sh createsuperuser`: Create superuser to access to admin at
[http://localhost:8000/admin/](http://localhost:8000/admin/)
  - `scripts/manage.sh shell_plus`: Interactive shell_plus to access db, query, e.t.c.
- For a full list of Django utilities command, take a look at:
  - [Django official command](https://docs.djangoproject.com/en/4.2/ref/django-admin/)
  - [Django extension command](https://django-extensions.readthedocs.io/en/latest/command_extensions.html)

### Packages management
- [uv](https://docs.astral.sh/uv/): the package dependencies management we use.
- When you want to add a dependency just run `uv add your_package_name`.

### Code conventions
- For code convention we are using:
  - [Ruff](https://pypi.org/project/ruff/): for speedy combination code formatting with flake8, blake or isort, e.t.c.
- The above tool have been wrapped with the executable script [scripts/lint.sh](scripts/lint.sh):
  - To lint only, run: `scripts/lint.sh`
  - To automatically format, run: `scripts/lint.sh --fix`

### Pre-commit hook
- To run these scripts automatically every time you commit, you need to install the pre-commit hooks:
  - Command: `pre-commit install`
  - [Pre-commit documentation](https://pre-commit.com/): Take a look at the documentation for more information.
  - After that, every time you commit, the `pre-commit` hooks will run the command defined in
[.pre-commit-config.yaml](.pre-commit-config.yaml) for you.


## 6. Running tests
- Normal run:
```bash
pytest {{ cookiecutter.project_slug }}
```
- With coverage
```bash
pytest --cov-report term --cov={{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }}
```
