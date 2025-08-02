import pytest
from typer.testing import CliRunner

from template_cli_python import cli_mean


@pytest.fixture
def runner() -> CliRunner:
    """CliRunnerのフィクスチャ"""
    return CliRunner()


class TestMeanCommand:
    """template_cli_python.cli_meanのテスト"""

    def test_cli_mean_help(self, runner: CliRunner) -> None:
        """CLIのヘルプが正しく表示されることのテスト"""
        result = runner.invoke(cli_mean.app, ["--help"])
        assert result.exit_code == 0
        assert "Usage:" in result.stdout


class TestArithmeticMean:
    """算術平均のテスト"""

    def test_arithmetic_mean(self, runner: CliRunner) -> None:
        """算術平均が正しく計算されることのテスト"""
        result = runner.invoke(cli_mean.app, ["arithmetic", "1", "2"])
        assert result.exit_code == 0
        assert "1.5" in result.stdout


class TestGeometricMean:
    """幾何平均のテスト"""

    def test_geometric_mean(self, runner: CliRunner) -> None:
        """幾何平均が正しく計算されることのテスト"""
        result = runner.invoke(cli_mean.app, ["geometric", "4", "16"])
        assert result.exit_code == 0
        assert "8.0" in result.stdout


class TestHarmonicMean:
    """調和平均のテスト"""

    def test_harmonic_mean(self, runner: CliRunner) -> None:
        """調和平均が正しく計算されることのテスト"""
        result = runner.invoke(cli_mean.app, ["harmonic", "4", "6"])
        assert result.exit_code == 0
        assert "4.8" in result.stdout

    def test_harmonic_mean_with_zero(self, runner: CliRunner) -> None:
        """調和平均でゼロが含まれる場合のテスト"""
        result = runner.invoke(cli_mean.app, ["harmonic", "0", "60"])
        assert result.exit_code == 0
