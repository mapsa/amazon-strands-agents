from click.testing import CliRunner
from your_package.cli import main


def test_cli_greeting():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "ChatGPT"])

    assert result.exit_code == 0
    assert "Hello, ChatGPT!" in result.output
