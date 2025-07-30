"""平均値計算サブコマンド群"""

import typer

app = typer.Typer(
    help="平均値計算コマンド群",
    add_completion=False,
    rich_markup_mode=None,
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)


@app.command("arithmetic")
def arithmetic_mean(a: float, b: float) -> None:
    """2つの数値の平均を計算

    2つの数値を受け取り、その平均を表示します。

    * a: (float) 1st number
    * b: (float) 2nd number
    """
    typer.echo((a + b) / 2)


@app.command("geometric")
def geometric_mean(a: float, b: float) -> None:
    """2つの数値の幾何平均を計算

    2つの数値を受け取り、その幾何平均を表示します。

    * a: (float) 1st number
    * b: (float) 2nd number
    """
    typer.echo((a * b) ** 0.5)


@app.command("harmonic")
def harmonic_mean(a: float, b: float) -> None:
    """2つの数値の調和平均を計算

    2つの数値を受け取り、その調和平均を表示します。

    * a: (float) 1st number
    * b: (float) 2nd number
    """
    if a == 0 or b == 0:
        typer.echo("調和平均はゼロで割ることができません。")
        return
    typer.echo(2 * (a * b) / (a + b))


@app.callback()
def main() -> None:
    """Main"""
    return


if __name__ == "__main__":
    app()
