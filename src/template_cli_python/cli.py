"""コマンドラインインターフェースを提供する"""

import typer

import common.arithmetic_ops as ops
from template_cli_python.cli_mean import app as subapp

app = typer.Typer(
    help="CLI app",
    add_completion=False,
    rich_markup_mode="rich",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)


@app.command()
def add(lhs: int = 0, rhs: int = 0) -> None:
    """2つの数値の加算

    2つの数値をオプションで受け取り、その合計を表示します。

    $ typer1 add --lhs 2 --rhs 3
    -> 5

    * lhs: (int) Left-hand side number
    * rhs: (int) Right-hand side number
    """
    typer.echo(ops.add(lhs, rhs))


@app.command()
def sub(lhs: int, rhs: int) -> None:
    """2つの数値の減算

    2つの数値をポジション引数で受け取り、その差を表示します。

    $ typer1 sub 5 3
    -> 2

    * lhs: (int) Left-hand side number
    * rhs: (int) Right-hand side number
    """
    typer.echo(ops.sub(lhs, rhs))


# commnad()の引数によるコマンド名のリネーム
@app.command("mul")
def multiply(lhs: int = 0, rhs: int = 0) -> None:
    """2つの数値の乗算

    2つの数値をオプションで受け取り、その積を表示します。

    * lhs: (int) Left-hand side number
    * rhs: (int) Right-hand side number
    """
    typer.echo(ops.mul(lhs, rhs))


# Annotated typer.Optionを使用してオプション引数を定義
@app.command()
def div(
    lhs: int = typer.Option(1, "-x", "--dividend", help="Dividend"),
    rhs: int = typer.Option(..., help="Divisor (non-zero)"),
) -> None:
    """2つの数値の除算

    2つの数値をオプションで受け取り、その商を表示します。

    * dividend: (int) 被除数
    * divisor: (int) 除数 (ゼロでないこと)
    """
    typer.echo(ops.div(lhs, rhs))


@app.command()
def sum9(
    a: int = typer.Argument(..., help="1st number"),  # 必須ポジション引数
    b: int = typer.Argument(2, help="2nd number"),  # デフォルト値を持つポジション引数
    c: int = typer.Option(..., help="3rd number"),  # required option
    d: int = typer.Option(4, help="4th number"),  # デフォルト値付きオプション
    e: int = typer.Option(5, "-e", help="5th number"),  # ショートオプションのみ
    f: int = typer.Option(6, "-f", "--6th", help="6th number"),  # ショート・ロング両方
    g: int = typer.Option(7, "--7th", help="7th number"),  # ロングオプションのみ
    h: int = typer.Option(8, "-h", "--8th", help="8th number"),  # ショート・ロング両方
    i: int = typer.Option(
        9, "-i", "--9th", help="9th number", rich_help_panel="Other Options panel"
    ),  # オプションをグループ分け
) -> None:
    """9つの数値の加算

    9つの数値をポジション引数とオプション引数で受け取り、その合計を表示します。
    """
    typer.echo(a + b + c + d + e + f + g + h + i)


app.add_typer(subapp, name="mean", help="平均計算サブコマンド")


# サブコマンドではなくオプションとしてバージョンを表示するためのコールバック関数
def _version_callback(*, show_version: bool) -> None:
    if show_version:  # pragma: no cover
        print("0.1.0")
        raise typer.Exit()


@app.callback()
def main(
    *,
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        callback=_version_callback,
        is_eager=True,
        help="バージョンを表示して終了",
    ),
) -> None:
    """メイン関数"""
    return


if __name__ == "__main__":
    app()
