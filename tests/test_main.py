"""template_cli_python/__main__.pyのテスト"""

import subprocess
import sys
from unittest.mock import patch

import pytest


class TestMainModule:
    """__main__.pyのテスト"""

    def test_main_module_import(self) -> None:
        """__main__.pyが正常にimportできることのテスト"""
        # __main__.pyをインポートしてもエラーが発生しないことを確認
        try:
            import template_cli_python.__main__  # noqa: F401
        except ImportError as e:
            pytest.fail(f"Failed to import __main__.py: {e}")

    def test_main_module_execution_with_mock(self) -> None:
        """__main__.py実行時の動作をmockでテスト"""
        # __main__.pyの実行をシミュレート
        with patch("template_cli_python.cli.app") as mock_app:
            # __main__.pyの内容を直接実行
            exec(
                """
if __name__ == "__main__":
    from template_cli_python import cli
    cli.app()
""",
                {"__name__": "__main__"},
            )
            # cli.app()が呼ばれることを確認
            mock_app.assert_called_once()

    def test_main_module_no_execution_when_imported(self) -> None:
        """通常のimport時にはcli.app()が実行されないことのテスト"""
        with patch("template_cli_python.cli.app") as mock_app:
            # 通常のimportをシミュレート
            exec(
                """
if __name__ == "__main__":
    from template_cli_python import cli
    cli.app()
""",
                {"__name__": "template_cli_python.__main__"},
            )
            # 通常のimportではcli.app()は呼ばれない
            mock_app.assert_not_called()

    def test_main_module_structure(self) -> None:
        """__main__.pyの基本構造のテスト"""
        import template_cli_python.__main__ as main_module

        # __main__.pyはモジュールオブジェクトであることを確認
        assert main_module.__name__ == "template_cli_python.__main__"

        # __main__.pyにはファイルパスが設定されていることを確認
        assert hasattr(main_module, "__file__")
        assert main_module.__file__.endswith("__main__.py")

    def test_main_module_execution_via_python_m(self) -> None:
        """Python -m template_cli_python での実行テスト"""
        # 実際にサブプロセスでpython -m template_cli_pythonを実行
        result = subprocess.run(
            [sys.executable, "-m", "template_cli_python", "--help"],
            capture_output=True,
            text=True,
            timeout=10,
        )

        # 正常終了することを確認
        assert result.returncode == 0
        # ヘルプメッセージが含まれることを確認
        assert "Usage:" in result.stdout
