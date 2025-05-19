.PHONY: all test install dev clean aws-login
PYTHON = python3

-include .env

all: install aws-login
	@naming_agent --project-description "AI agent builder"

aws-login:
	@echo "Checking AWS SSO session..."
	@if ! aws sts get-caller-identity > /dev/null 2>&1; then \
		echo "AWS session expired. Refreshing..."; \
		aws sso login; \
	else \
		echo "AWS session is valid"; \
	fi

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