.PHONY: all test install dev clean
PYTHON = python3

-include .env

all: install
	@your-cli --name "World"

install:
	@echo "Installing/updating production dependencies..."
	@uv sync

test: dev
	pytest

dev: install
	@echo "Installing development dependencies..."
	@uv pip install -e .
	@pre-commit install
	@echo "Package installed. Run 'make test' to run tests."

clean:
	rm -rf .venv __pycache__ .pytest_cache *.egg-info