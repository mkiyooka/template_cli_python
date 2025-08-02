"""CLI機能のテスト"""

import pytest
from typer.testing import CliRunner

from template_cli_python.cli import app


@pytest.fixture
def runner() -> CliRunner:
    """CliRunnerのフィクスチャ"""
    return CliRunner()


class TestAddCommand:
    """addコマンドのテスト"""

    def test_add_with_options(self, runner: CliRunner) -> None:
        """オプション引数でのaddコマンドテスト"""
        result = runner.invoke(app, ["add", "--lhs", "2", "--rhs", "3"])
        assert result.exit_code == 0
        assert "5" in result.stdout

    def test_add_with_defaults(self, runner: CliRunner) -> None:
        """デフォルト値でのaddコマンドテスト"""
        result = runner.invoke(app, ["add"])
        assert result.exit_code == 0
        assert "0" in result.stdout

    def test_add_partial_options(self, runner: CliRunner) -> None:
        """一部のオプションのみ指定でのaddコマンドテスト"""
        result = runner.invoke(app, ["add", "--lhs", "5"])
        assert result.exit_code == 0
        assert "5" in result.stdout


class TestSubCommand:
    """subコマンドのテスト"""

    def test_sub_with_positional_args(self, runner: CliRunner) -> None:
        """ポジション引数でのsubコマンドテスト"""
        result = runner.invoke(app, ["sub", "5", "3"])
        assert result.exit_code == 0
        assert "2" in result.stdout

    def test_sub_negative_result(self, runner: CliRunner) -> None:
        """負の結果のsubコマンドテスト"""
        result = runner.invoke(app, ["sub", "3", "5"])
        assert result.exit_code == 0
        assert "-2" in result.stdout

    def test_sub_missing_args(self, runner: CliRunner) -> None:
        """引数不足でのsubコマンドテスト"""
        result = runner.invoke(app, ["sub", "5"])
        assert result.exit_code != 0


class TestMulCommand:
    """mulコマンドのテスト"""

    def test_mul_with_options(self, runner: CliRunner) -> None:
        """オプション引数でのmulコマンドテスト"""
        result = runner.invoke(app, ["mul", "--lhs", "3", "--rhs", "4"])
        assert result.exit_code == 0
        assert "12" in result.stdout

    def test_mul_with_defaults(self, runner: CliRunner) -> None:
        """デフォルト値でのmulコマンドテスト"""
        result = runner.invoke(app, ["mul"])
        assert result.exit_code == 0
        assert "0" in result.stdout


class TestDivCommand:
    """divコマンドのテスト"""

    def test_div_with_options(self, runner: CliRunner) -> None:
        """オプション引数でのdivコマンドテスト"""
        result = runner.invoke(app, ["div", "--dividend", "6", "--divisor", "3"])
        assert result.exit_code == 0
        assert "2" in result.stdout

    def test_div_with_default_dividend(self, runner: CliRunner) -> None:
        """被除数デフォルト値でのdivコマンドテスト"""
        result = runner.invoke(app, ["div", "--divisor", "0"])
        assert result.exit_code == 0
        assert "Division by zero is not allowed." in result.stderr


class TestSum9Command:
    """sum9コマンドのテスト"""

    def test_sum9_with_minimal_args(self, runner: CliRunner) -> None:
        """最小限の引数でのsum9コマンドテスト"""
        result = runner.invoke(app, ["sum9", "1", "--c", "3"])
        assert result.exit_code == 0
        assert "45" in result.stdout

    def test_sum9_missing_required_args(self, runner: CliRunner) -> None:
        """必須引数不足でのsum9コマンドテスト"""
        result = runner.invoke(app, ["sum9"])
        assert result.exit_code != 0


class TestVersionOption:
    """バージョンオプションのテスト"""

    def test_version_long_option(self, runner: CliRunner) -> None:
        """--versionオプションのテスト"""
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "Version:" in result.stdout

    def test_version_short_option(self, runner: CliRunner) -> None:
        """-vオプションのテスト"""
        result = runner.invoke(app, ["-v"])
        assert result.exit_code == 0
        assert "Version:" in result.stdout


class TestHelpOption:
    """ヘルプオプションのテスト"""

    def test_main_help(self, runner: CliRunner) -> None:
        """メインコマンドのヘルプテスト"""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "CLI app" in result.stdout
        assert "add" in result.stdout
        assert "sub" in result.stdout
        assert "mul" in result.stdout
        assert "div" in result.stdout

    def test_add_help(self, runner: CliRunner) -> None:
        """addコマンドのヘルプテスト"""
        result = runner.invoke(app, ["add", "--help"])
        assert result.exit_code == 0
        assert "2つの数値の加算" in result.stdout

    def test_sub_help(self, runner: CliRunner) -> None:
        """subコマンドのヘルプテスト"""
        result = runner.invoke(app, ["sub", "--help"])
        assert result.exit_code == 0
        assert "2つの数値の減算" in result.stdout


class TestSubcommand:
    """サブコマンドのテスト"""

    def test_mean_subcommand_exists(self, runner: CliRunner) -> None:
        """meanサブコマンドの存在確認"""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "mean" in result.stdout

    def test_mean_subcommand_help(self, runner: CliRunner) -> None:
        """meanサブコマンドのヘルプテスト"""
        result = runner.invoke(app, ["mean", "--help"])
        assert result.exit_code == 0

    def test_arithmetic_mean(self, runner: CliRunner) -> None:
        """算術平均のテスト"""
        result = runner.invoke(app, ["mean", "arithmetic", "1", "2"])
        assert result.exit_code == 0
        assert "1.5" in result.stdout

    def test_geometric_mean(self, runner: CliRunner) -> None:
        """幾何平均のテスト"""
        result = runner.invoke(app, ["mean", "geometric", "4", "16"])
        assert result.exit_code == 0
        assert "8.0" in result.stdout

    def test_harmonic_mean(self, runner: CliRunner) -> None:
        """調和平均のテスト"""
        result = runner.invoke(app, ["mean", "harmonic", "4", "6"])
        assert result.exit_code == 0
        assert "4.8" in result.stdout

    def test_harmonic_mean_with_zero(self, runner: CliRunner) -> None:
        """調和平均でゼロが含まれる場合のテスト"""
        result = runner.invoke(app, ["mean", "harmonic", "0", "60"])
        assert result.exit_code == 0


class TestInvalidCommands:
    """無効なコマンドのテスト"""

    def test_invalid_command(self, runner: CliRunner) -> None:
        """存在しないコマンドのテスト"""
        result = runner.invoke(app, ["invalid_command"])
        assert result.exit_code != 0

    def test_no_args_shows_help(self, runner: CliRunner) -> None:
        """引数なしでヘルプが表示されることのテスト"""
        result = runner.invoke(app, [])
        assert result.exit_code == 2  # no_args_is_help=Trueの場合は2で終了
        assert "CLI app" in result.stdout
