# Strands Agents Example

A demonstration project that showcases how to build AI agents using Amazon Strands Framework with Amazon Bedrock models.

## Features

- **Project Name Generator**: An AI agent that suggests names for open source projects
- **Domain & GitHub Validation**: Checks if suggested domain names and GitHub organizations are available
- **Strands Integration**: Uses the Amazon Strands Agent Framework
- **Bedrock Models**: Leverages Amazon Bedrock foundation models
- **MCP Server**: Utilizes Model Context Protocol server for tool execution
- **CLI Support**: Provides a convenient command-line interface

## Project Structure

```
.
├── Makefile               # Build automation
├── pyproject.toml         # Project metadata and dependencies
├── README.md              # This file
├── src/                   # Source code
│   ├── notebooks/         # Jupyter notebooks for exploration
│   └── strands_agents_example/ # Main package
│       ├── __init__.py
│       ├── agent.py       # Agent implementation
│       └── cli.py         # Command-line interface
└── tests/                 # Test suite
    └── test_cli.py        # CLI tests
```

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- AWS credentials with Bedrock access
- GitHub personal access token for GitHub organization validation

## Getting Started

### Environment Setup

1. Create a `.env` file by copying the example:

```bash
cp .env.example .env
```

2. Add your GitHub personal access token to the `.env` file:

```bash
# In .env file
GITHUB_TOKEN=your_github_token_here
```

You can generate a new GitHub token at [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/personal-access-tokens). The token needs at least `read:org` scope to check organization availability.

### AWS Account Setup

1. Ensure you have an AWS account with access to Amazon Bedrock.

1. Configure AWS SSO for authentication:

   ```bash
   # Configure AWS SSO
   aws configure sso
   # Follow the prompts to set up your SSO profile
   ```

1. Verify your AWS profile has the following permissions:

   - `bedrock:InvokeModel`
   - `bedrock:InvokeModelWithResponseStream`

1. You can refresh your AWS SSO session anytime using:

   ```bash
   make aws-login
   ```

1. To use a specific AWS profile, add the following to your `.env` file:

   ```bash
   # In .env file
   AWS_PROFILE=your_aws_profile_name
   ```

### Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/yourusername/amazon-strands-agents.git
cd amazon-strands-agents
make install
```

For development setup (includes test dependencies):

```bash
make dev
```

### Usage

Run the project naming agent:

```bash
naming_agent --project-description "your project description"
```

Or through make (uses a default description):

```bash
make
```

## How It Works

This example showcases how to create an AI agent using the Strands framework that:

1. Takes a project description as input
1. Generates potential project names
1. Validates domain name availability using a custom MCP server
1. Verifies GitHub organization name availability using HTTP requests
1. Returns suggestions for available project names

The agent is composed of:

- A system prompt that defines the agent's behaviour
- Tools for domain name and GitHub availability checking
- Integration with Amazon Bedrock for text generation

## Customizing the Project

1. Update project information in `pyproject.toml`
1. Modify the system prompt in `agent.py` to change agent behaviour
1. Add new tools to enhance agent capabilities
1. Implement additional CLI commands for more functionality

## Development Workflow

1. **Setup**:
   - `make dev` installs all dependencies and pre-commit hooks
   - Create and configure your `.env` file with required tokens
1. **AWS Authentication**: `make aws-login` sets up your AWS SSO session
1. **Development**:
   - Write agent code in `src/strands_agents_example/`
   - Create tests in `tests/`
   - Use notebooks in `src/notebooks/` for exploration
1. **Testing**: `make test` runs all tests

## Dependencies

- **Core**: strands-agents, strands-agents-tools
- **CLI**: click
- **Development**: pytest, ruff, black, isort, pre-commit, ipykernel, ipywidgets

______________________________________________________________________

*For more information about Amazon Strands, visit [Amazon Strands SDK](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/).*
