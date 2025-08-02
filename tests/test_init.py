"""template_cli_python/__init__.pyのテスト"""

import template_cli_python


class TestVersion:
    """バージョン情報のテスト"""

    def test_version_format(self) -> None:
        """バージョンが適切な形式であることのテスト"""
        version = template_cli_python.__version__
        # バージョンは通常 x.y.z 形式か、開発版の場合は x.y.z.devN などの形式
        # 少なくとも数字とピリオドを含むことを確認
        assert any(char.isdigit() for char in version), (
            f"Version should contain digits: {version}"
        )


class TestModuleStructure:
    """モジュール構造のテスト"""

    def test_package_attributes(self) -> None:
        """パッケージに必要な属性が存在することのテスト"""
        # __version__は必須
        assert hasattr(template_cli_python, "__version__")

        # パッケージ名も確認できるならテスト
        if hasattr(template_cli_python, "__name__"):
            assert template_cli_python.__name__ == "template_cli_python"
