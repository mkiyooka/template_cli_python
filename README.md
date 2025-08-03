# Python CLI application template

## 利用者向けの説明

### インストールとサンプルコマンドの実行方法

このプロジェクトをパッケージとしてインストールするには以下の手順を実行してください。

```sh
git clone https://github.com/mkiyooka/template_cli_python.git
cd template_cli_python
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

gitリポジトリから直接インストールするには以下のコマンドを実行してください。

```sh
pip install git+https://github.com/mkiyooka/template_cli_python.git
```

サンプルコマンドの実行方法

```sh
# 四則演算や平均計算など、すべての機能は main_app コマンドで利用できます。
main_app --help
# 次のコマンドでモジュールとして呼び出すこともできます。
python -m template_cli_python --help
```

アンインストール方法

```sh
pip uninstall template-cli-python
rm -rf template_cli_python
```

### uv向け

パッケージのインストールだけであれば`venv`と`pip`のみで実行可能です。

```sh
git clone https://github.com/mkiyooka/template_cli_python.git
cd template_cli_python
uv venv
source .venv/bin/activate
uv pip install .
```

## 開発者向けガイド

- [基本](docs/development-guide-basic.md)
- [開発用ツール導入](docs/development-guide-tools.md)
