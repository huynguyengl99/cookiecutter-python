#!/usr/bin/env bash

set -e

export PYTHONPATH=":{{ cookiecutter.project_slug }}"


# Cleaning existing cache:
if [ "$1" == "-nc" ]; then
  rm -rf .mypy_cache
fi


mypy {{ cookiecutter.project_slug }}
