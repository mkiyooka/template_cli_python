# Zed Configuration for Python Development

このプロジェクトのZed設定を説明します。

## このディレクトリの設定

- `settings.json`: LSP（pyright、ruff）、言語設定、ファイル除外設定
- `tasks.json`: uv経由のタスク（test、lint、format等）
- `debug.json`: debugpyを使ったデバッグ設定

## ローカル設定（ユーザーグローバル設定）

以下の設定は `~/.config/zed/settings.json` に追加してください。

```json
{
    "terminal": {
        "copy_on_select": true
    }
}
```

## 開発ワークフロー

1. 初回セットアップ: `uv sync`（タスクから実行可能）
2. タスク実行: Cmd+Shift+P -> "task: spawn"
3. デバッグ実行: Cmd+Shift+P -> "debug: ..."

## 利用可能なタスク

| ラベル | 内容 |
| --- | --- |
| `uv sync` | 依存関係のインストール |
| `pytest` | テスト実行（カバレッジ付き） |
| `ruff format` | コードフォーマット |
| `ruff check` | リント（自動修正付き） |
| `pyright` | 型チェック |
| `fullcheck` | 全品質チェック（format + lint + typecheck + test） |
| `run app` | CLIアプリの実行 |
