# 開発ガイドライン

このドキュメントは、プロジェクトでの開発作業において従うべき重要なガイドラインを説明します。これらのガイドラインを正確に守ってください。

## 基本開発ルール

1. パッケージ管理
    - **ONLY use uv, NEVER pip**
    - インストール: `uv add <package-name>`
    - ツール実行: `uv run tool`
    - アップグレード: `uv add --dev <package-name> --upgrade-package <package-name>`
    - **禁止**: `uv pip install`, `@latest` 構文
2. コード品質
    - すべてのコードに型ヒントが必要
    - パブリック API には docstring が必須
    - 関数は集中的で小さく保つ
    - 既存のパターンに正確に従う
    - 行の長さ: 最大88文字
3. テスト要件
    - フレームワーク: `uv run --frozen pytest`
    - カバレッジ: エッジケースとエラーをテスト
    - 新機能にはテストが必要
    - バグ修正には回帰テストが必要
4. コミット
    - コミット前にテストとコード品質をチェック
    - 目的毎にコミットを分割して、変更を最小限に保つ

### `--frozen`オプションについて

`uv run --frozen` は依存関係の解決をスキップし、ロックファイル（`uv.lock`）から直接実行します。これにより以下の効果があります。

- **実行速度の向上**: 依存関係の再解決が不要
- **再現性の確保**: 常に同じバージョンの依存関係を使用
- **CI環境での安定性**: 予期しない依存関係の変更を防止

開発中は基本的に `--frozen` を使用してください。

## コードフォーマット

1. Ruff
    - フォーマット: `uv run --frozen ruff format .`
    - チェック: `uv run --frozen ruff check .`
    - 修正: `uv run --frozen ruff check . --fix`
    - 重要な問題:
        - 行の長さ (88文字)
        - インポートの並び替え (I001)
        - 未使用のインポート
    - 行の折り返し:
        - 文字列: 括弧を使用
        - 関数呼び出し: 適切なインデントで複数行
        - インポート: 複数行に分割
2. 型チェック
    - ツール: `uv run --frozen pyright`
    - 要件:
        - Optional の明示的な None チェック
        - 文字列の型ナローイング
        - チェックが通る場合、バージョン警告は無視可能
3. Pre-commit
    - 設定: `.pre-commit-config.yaml`
    - 実行: git commit 時
    - ツール: Prettier (YAML/JSON), Ruff (Python)

## コミットとプルリクエスト

### コミットメッセージ

Conventional Commits形式に従ってコミットメッセージを作成してください。

> **ツールの使用方法**: Commitizenツールの具体的な使用方法については、[development-guide-tools.md](./development-guide-tools.md#commitizen) を参照してください。

#### 基本形式

```text
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

`(<scope>)`は省略可能。

#### 見出し行の例

```text
feat: データ処理機能を追加
^--^  ^------------^
|     |
|     +-> 現在形で要約を記載する。(「データ処理機能を追加」「データ処理機能を追加する」)
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```

#### type

以下のtypeの中からいずれかを記載する。互換性のない機能変更をした場合は`!`を後ろにつける。

- `feat`: 新機能の追加（ユーザー向けの新機能、ビルドスクリプトの新機能ではない）
- `fix`: バグ修正（ユーザー向けのバグ修正、ビルドスクリプトの修正ではない）
- `docs`: ドキュメントのみの変更
- `style`: コードの動作に影響しない変更（フォーマット、セミコロンの欠落など、本番コードの変更なし）
- `refactor`: 本番コードのリファクタリング（例：変数名の変更、バグ修正でも機能追加でもない）
- `test`: 不足していたテストの追加や既存テストの修正（本番コードの変更なし）
- `chore`: uv buildやmakeタスクの更新など（本番コードの変更なし、依存関係の更新、ビルドツールの変更）

#### Scope

プロジェクトごとにScopeを定義して、必要に応じてtypeの後ろに記載する。
Angularで採用されているScopeの一例を示す。

- **common**
- **core**
- **elements**
- **forms**
- **http**
- **language-service**
- **localize**
- **router**
- **service-worker**

#### コミットメッセージ例

- ワンラインコメント

    ```text
    feat(cli): データ処理用のサブコマンドを追加
    ```

    破壊的変更の場合はtypeの後ろに`!`をつけます。

    ```text
    feat(cli)!: データ初利用のコマンド名を変更
    ```

    ```text
    docs: インストールガイドを記載
    ```

- 複数行コメント

    ```text
    feat(cli): データ処理用のサブコマンドを追加

    - ヒストグラム生成(hist)機能を追加
    - 外れ値検出(oulier)機能を追加
    ```

### プルリクエスト

- 変更内容の詳細なメッセージを作成
- 解決しようとする問題と解決方法の高レベルな説明に焦点
- 明確性を追加する場合を除き、コードの詳細には触れない

## 開発環境設定

### 必要なツール

- **uv**: パッケージ管理
- **ruff**: フォーマットとリンティング
- **pyright**: 型チェック
- **pytest**: テストフレームワーク
- **pre-commit**: コミット時自動チェック

### セットアップ手順

```bash
# 依存関係のインストール
uv sync

# pre-commit のセットアップ
uv run pre-commit install

# 開発用ツールの実行例
uv run --frozen ruff format .
uv run --frozen ruff check .
uv run --frozen pyright
uv run --frozen pytest
```

## 継続的インテグレーション

### 品質チェック

プロジェクトでは以下の品質チェックが自動実行されます:

1. **コミット時** (pre-commit):
   - Ruff フォーマット・チェック
   - Commitizen メッセージ形式チェック

2. **プッシュ時** (CI):
   - 全環境でのテスト実行
   - カバレッジ計測
   - 型チェック

### 推奨ワークフロー

```bash
# 1. 変更を実装
# 2. フォーマットとチェック
uv run --frozen ruff format .
uv run --frozen ruff check . --fix

# 3. 型チェック
uv run --frozen pyright

# 4. テスト実行
uv run --frozen pytest

# 5. コミット（pre-commit が自動実行）
git add .
git commit -m "feat: 新機能の説明"

# 6. プッシュ
git push
```

このガイドラインに従うことで、一貫性のある高品質なコードベースを維持できます。
