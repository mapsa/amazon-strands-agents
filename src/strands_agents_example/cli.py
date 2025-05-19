import click

from strands_agents_example.agent import run_naming_agent


@click.command()
@click.option(
    "--project-description",
    default="build AI agents",
    help="Description of the project.",
)
def main(project_description):
    """Simple CLI that greets NAME."""
    response = run_naming_agent(project_description)
    click.echo(f"Project name suggestion: {response}")
