# Contributing to {{  cookiecutter.project_name }}

Contributions are welcome! Here are some pointers to help you install the library for development and validate your changes before submitting a pull request.

## Install the library for development

First create your own `.venv` and activate it:

```bash
pythin -m venv .venv
source .venv/bin/activate
```

Then we recommend installing initial requirements and use poetry install all dev package:
```bash
pip install -r requirements-init.txt
poetry install --all-extras
```

## Validate the changes before creating a pull request
{% if cookiecutter.use_docker %}
0. Prepare for test:
- Docker running
- Run `docker-compose up` to create testing postgresql database.

{% endif %}
1. Make sure the existing tests are still passing (and consider adding new tests as well!):

```bash
pytest --cov-report term-missing --cov={{ cookiecutter.project_slug }} tests
```

2. Reformat and validate the code with the following tools:

```bash
bash scripts/lint.sh [--fix]
```

3. For committing code, use the [Commitizen](https://commitizen-tools.github.io/commitizen/) tool to follow
commit best practices.

```bash
cz commit
```

These steps are also run automatically in the CI when you open the pull request.
