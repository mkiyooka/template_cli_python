"""コマンドラインインターフェースを提供する"""

import typer
from rich import print as rprint

app = typer.Typer(
    help="CLI app",
    add_completion=False,
    rich_markup_mode="markdown",
    pretty_exceptions_enable=False,
)


@app.command()
def add(lhs: int = 0, rhs: int = 0) -> None:
    """Add two numbers.

    * lhs: (int) Left-hand side number

    * rhs: (int) Right-hand side number
    """
    typer.echo(lhs + rhs)
    rprint([lhs + rhs, "hello"])


@app.command("mul")
def multiply(lhs: int = 0, rhs: int = 0) -> None:
    """Multiply two numbers.

    * lhs: (int) Left-hand side number

    * rhs: (int) Right-hand side number
    """
    rprint(lhs * rhs)


@app.callback()
def main() -> None:
    """Main"""
    return


def main_cli() -> None:
    """CLIエントリーポイント"""
    app()


if __name__ == "__main__":
    main_cli()
