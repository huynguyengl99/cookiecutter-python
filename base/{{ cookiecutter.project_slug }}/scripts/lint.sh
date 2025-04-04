#!/usr/bin/env bash

if [ "$1" == "--fix" ]; then
  ruff check . --fix && black ./{{ cookiecutter.project_slug }} && toml-sort ./*.toml
else
  ruff check . && black ./{{ cookiecutter.project_slug }} --check && toml-sort ./*.toml --check
fi
