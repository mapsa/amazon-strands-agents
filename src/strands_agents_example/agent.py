## Strands Agents SDF Example
# Helper to name projects. Components:
# 1) Model: Amazon Bedrock
# 2) Tools: pre-build Strands Tools + MCP server
# 3) Prompt:

from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands.tools.mcp import MCPClient
from strands_tools import http_request

# Define a naming-focused system prompt
NAMING_SYSTEM_PROMPT = """
You are an assistant that helps to name open source projects.

When providing open source project name suggestions, always provide
one or more available domain names and one or more available GitHub
organization names that could be used for the project.

Before providing your suggestions, use your tools to validate
that the domain names are not already registered and that the GitHub
organization names are not already used.
"""


def get_domain_name_tools():
    """
    Create and return an MCPClient instance for domain name availability checking.

    Returns:
        MCPClient: A client for the domain name checking MCP server.
    """
    return MCPClient(
        lambda: stdio_client(
            StdioServerParameters(
                command="uvx", args=["fastdomaincheck-mcp-server"]
            )
        )
    )


def get_github_tools():
    """
    Get the pre-built GitHub API tools.

    Returns:
        list: A list of GitHub related tools.
    """
    return [http_request]


def create_naming_agent(domain_name_tools, github_tools):
    """
    Create a Strands Agent for project naming.

    Args:
        domain_name_tools (MCPClient): The tools for checking domain name availability.
        github_tools (list): The tools for GitHub organization checking.

    Returns:
        Agent: A configured Strands agent for project naming.
    """
    tools = domain_name_tools.list_tools_sync() + github_tools
    return Agent(system_prompt=NAMING_SYSTEM_PROMPT, tools=tools)


def run_naming_agent(prompt):
    """
    Run the naming agent with the given prompt.

    Args:
        prompt (str): The end user's prompt.

    Returns:
        str: The agent's response.
    """
    domain_name_tools = get_domain_name_tools()
    github_tools = get_github_tools()

    with domain_name_tools:
        agent = create_naming_agent(domain_name_tools, github_tools)
        return agent(prompt)
