#!/bin/sh

echo "## Run flake8"
flake8 app
flake8 core
flake8 tests

echo "## Run black"
black .

echo "## Run isort"
isort
