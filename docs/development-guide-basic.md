# 開発環境セットアップガイド

このドキュメントでは、開発を始めるための最小限のセットアップと、コミット前に必要な品質チェックについて説明します。

## 最小セットアップ（3ステップ）

### 1. uvのインストール

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. プロジェクトのセットアップ

```sh
git clone https://github.com/mkiyooka/template_cli_python.git
cd template_cli_python
uv sync --all-groups
source .venv/bin/activate
```

### 3. pre-commitの設定

```sh
uvx pre-commit install
```

これで開発を開始できます。VS Codeでファイルを開けば、自動的にコード品質チェックが有効になります。

## コミット前の品質チェック

コードをコミットする前に、以下の品質チェックを実行してください。

### 必須チェック（4つ）

```sh
# 1. コードフォーマット
uv run --frozen ruff format .

# 2. リント・品質チェック
uv run --frozen ruff check . --fix

# 3. 型チェック
uv run --frozen pyright

# 4. テスト実行
uv run --frozen pytest --cov=template_cli_python --cov-report=term
```

### 一括実行

すべてのチェックを一度に実行する場合：

```sh
# taskipyを使用した一括実行
uv run task check

# CI環境相当の実行
uv run nox
```

## コード整形・リント・テストの自動化

### VS Code

ファイルを開くだけで自動的に以下が実行されます：

- 保存時のコードフォーマット（Ruff）
- リアルタイム型チェック（Pyright）
- エラー・警告の表示

### Pre-commit

`git commit`時に自動的に以下が実行されます：

- Ruffによる品質チェック（リント・フォーマット）
- Pyrightによる型チェック
- Pytestによるテスト実行
- コミットメッセージの形式チェック

エラーが発生した場合は、修正してから再度コミットしてください。

## よくある問題と解決方法

### 依存関係の問題

```sh
uv sync --reinstall
```

### 型チェックエラー

```sh
# 詳細なエラー情報を表示
uv run --frozen pyright --verbose
```

### テストの失敗

```sh
# 詳細なテスト出力
uv run --frozen pytest -v

# 最初の失敗で停止
uv run --frozen pytest -x
```

## 詳細情報

- **ツールの詳細設定**: [development-guide-tools.md](./development-guide-tools.md)
- **開発ガイドライン**: [development-guidelines.md](./development-guidelines.md)
