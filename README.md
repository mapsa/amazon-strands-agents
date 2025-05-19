# Python Project Template

A modern Python project template that provides a standardized structure for Python development with best practices for dependency management, code quality, and automation.

## Features

- **Modern Structure**: Clear separation between source code, tests, and notebooks
- **Package Management**: Uses [uv](https://github.com/astral-sh/uv) for fast, reliable package management
- **Dependency Management**: Centralized in `pyproject.toml` following PEP 621
- **Build Automation**: Makefile with common development tasks
- **Code Quality**: Pre-commit hooks for consistent code quality
- **CLI Support**: Ready-to-use [Click](https://click.palletsprojects.com/) command-line interface
- **Testing**: Pytest setup with example tests

## Project Structure

```
.
├── Makefile               # Build automation
├── pyproject.toml         # Project metadata and dependencies
├── README.md              # This file
├── src/                   # Source code
│   ├── notebooks/         # Jupyter notebooks
│   └── your_package/      # Main package
│       ├── __init__.py
│       └── cli.py         # Command-line interface
└── tests/                 # Test suite
    └── test_cli.py        # CLI tests
```

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

## Getting Started

### Installation

Clone this template and install dependencies:

```bash
git clone https://github.com/yourusername/python-project-template.git
cd python-project-template
make install
```

For development setup (includes test dependencies):

```bash
make dev
```

### Usage

Run the sample CLI:

```bash
your-cli --name "YourName"
```

Or through make:

```bash
make
```

### Testing

Run tests with:

```bash
make test
```

## Customizing the Template

1. Update project information in `pyproject.toml`:

   - Change `name`, `version`, `description`
   - Update `authors` with your information
   - Modify `dependencies` as needed

1. Rename directories:

   - Change `src/your_package` to your actual package name
   - Update imports in all files

1. Update CLI:

   - Modify `src/your_package/cli.py` with your actual commands
   - Update `[project.scripts]` in `pyproject.toml` with your CLI name

## Development Workflow

This template supports a smooth development workflow:

1. **Setup**: `make dev` installs all dependencies and pre-commit hooks
1. **Development**:
   - Write code in `src/your_package/`
   - Create tests in `tests/`
   - Use notebooks in `src/notebooks/` for exploration
1. **Code Quality**: Pre-commit hooks enforce:
   - Code formatting with Black
   - Import sorting with isort
   - Linting with Ruff
1. **Testing**: `make test` runs all tests

## Package Details

- **Dependencies**:

  - Runtime: click
  - Development: pytest, ruff, black, isort, pre-commit, ipykernel, ipywidgets

- **Build System**: Uses hatchling for package building

- **Python Version**: Requires Python 3.12+

______________________________________________________________________

*To use this template, fork or clone this repository and customize it for your project.*
