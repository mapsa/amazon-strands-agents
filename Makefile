.PHONY: all test install dev clean aws-login
PYTHON = python3

-include .env

all: install aws-login
	@naming_agent --project-description "AI agent builder"

aws-login:
	@echo "Refreshing AWS SSO session..."
	@aws sso login

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