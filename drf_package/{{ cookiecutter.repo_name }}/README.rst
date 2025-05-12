{{ cookiecutter.project_name|upper }}
{{ '=' * cookiecutter.project_name|length }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}
   :target: https://pypi.org/project/{{ cookiecutter.repo_name }}/
   :alt: PyPI

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: Code Coverage

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions/workflows/test.yml/badge.svg?branch=main
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions/workflows/test.yml
   :alt: Test

.. image:: https://www.mypy-lang.org/static/mypy_badge.svg
   :target: https://mypy-lang.org/
   :alt: Checked with mypy

.. image:: https://microsoft.github.io/pyright/img/pyright_badge.svg
   :target: https://microsoft.github.io/pyright/
   :alt: Checked with pyright

.. image:: https://chanx.readthedocs.io/en/latest/_static/interrogate_badge.svg
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: Docstring

{{ cookiecutter.description }}

Installation
------------

.. code-block:: bash

    pip install {{ cookiecutter.repo_name }}

Documentation
-------------

Please visit `{{ cookiecutter.project_name }} docs <https://{{ cookiecutter.repo_name }}.readthedocs.io/>`_ for
complete documentation.
