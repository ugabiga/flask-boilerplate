#!/bin/sh

echo "## Run mypy"
mypy .
echo ""

echo "## Run flake8"
flake8 app
flake8 core
flake8 tests
echo "done"
echo ""

echo "## Run black"
black .
echo ""

echo "## Run isort"
isort
