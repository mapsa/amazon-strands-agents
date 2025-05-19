import click


@click.command()
@click.option('--name', default='world', help='Name to greet.')
def main(name):
    """Simple CLI that greets NAME."""
    click.echo(f"Hello, {name}!")
