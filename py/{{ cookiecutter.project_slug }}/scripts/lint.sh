#!/usr/bin/env bash

if [ "$1" == "--fix" ]; then
  ruff check . --fix && black ./src && toml-sort ./*.toml
else
  ruff check . && black ./src --check && toml-sort ./*.toml --check
fi
