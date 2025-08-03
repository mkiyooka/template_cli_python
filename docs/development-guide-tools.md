# 開発用ツールの詳細ガイド

このドキュメントでは、Python開発プロジェクトで使用する開発ツールの詳細な機能と設定について説明します。

## このドキュメントで説明する内容

- パッケージ管理ツール
    - **uv**: 高速なPythonパッケージマネージャー（依存関係管理、仮想環境管理）
- コード品質チェックツール
    - **Ruff**: 高速なリンター・フォーマッター（コードスタイル統一、品質チェック）
    - **Pyright**: 静的型チェッカー（型安全性の確保）
    - **pytest**: テスティングフレームワーク（単体テスト実行）
    - **coverage**: コードカバレッジ測定（テスト網羅性の確認）
- プロジェクト管理ツール
    - **Commitizen**: コミットメッセージの標準化とバージョン管理（Conventional Commits形式）
- 自動化・統合ツール
    - **taskipy**: タスクランナー（複数コマンドの簡易実行）
    - **Nox**: CI/CD環境相当の隔離実行環境
    - **pre-commit**: コミット時の自動品質チェック
    - **VS Code**: エディタ統合（リアルタイム品質チェック）

## ツール間の呼び出し関係

以下の表は、各実行方法からどの品質チェックツールが呼び出されるかを示しています：

| 実行方法 ＼ 実行ツール | Ruff | Pyright | pytest | Commitizen |
|:---|:---|:---|:---|:---|
| **VS Code** | ✅ 保存時/編集時 | ✅ リアルタイム | ✅ テスト機能 | ❌ |
| **pre-commit** | ✅ コミット時 | ✅ コミット時 | ✅ コミット時 | ✅ コミット時 |
| **uv run** | ✅ 直接実行 | ✅ 直接実行 | ✅ 直接実行 | ✅ 直接実行 |
| **taskipy** | ✅ task format/lint | ✅ task typecheck | ✅ task test | ❌ |
| **Nox** | ✅ lint セッション | ✅ pyright セッション | ✅ coverage セッション | ❌ |

### 実行方法の特徴

- **VS Code**: 開発中のリアルタイムチェック（最も頻繁に使用）
- **pre-commit**: コミット時の自動品質ゲート（品質保証）
- **直接実行 (uv run)**: 個別ツールの直接実行（デバッグ・詳細確認）
- **taskipy**: 開発者の手動実行用（中間チェック）
- **Nox**: CI/CD環境相当（最終検証）

## 開発ツールの紹介

このプロジェクトでは、**Python開発**におけるコード品質の向上とテストの自動化のために以下のツールを利用しています：

### パッケージ管理ツール

#### uv

**機能**: 高速なPythonパッケージマネージャー・プロジェクト管理ツール

- Python環境の管理とパッケージのインストール
- 依存関係の解決と仮想環境の自動管理
- 従来のpip/pipenvよりも高速な動作
- プロジェクトの依存関係をlockファイル(uv.lock)で管理

インストール方法:

```sh
# macOS/Linux/Windows(Git Bash for Windows)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**自動補完の設定 (bashの場合)**:

```sh
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc
```

**自動補完の設定 (zshの場合)**:

```sh
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```

**基本的な使用方法**:

```sh
# アプリケーションプロジェクト作成
uv init --app <project-name>

# アプリケーションとパッケージ提供の両方
uv init --app --package <project-name>

# 依存関係のインストール
uv sync

# パッケージの追加
uv add <package-name>

# 開発依存関係の追加
uv add --group dev <package-name>

# --group devの代わりに--devオプションも利用できます。
uv add --dev <package-name>

# 仮想環境でコマンド実行
uv run <command>

# 依存関係を固定してコマンド実行
uv run --frozen <command>

# Python REPL の起動
uv run python

# ツールのインストールと実行 (プロジェクトディレクトリの.venvとは別にインストールされる)
uv tool run <tool-name>

# 次のように実行します。
uv tool run pre-commit

# プロジェクト名とコマンドが異なる場合は--fromオプションでパッケージ名を指定します。
uv tool run --from commitizen cz --help
```

**プロジェクト管理の特徴**:

- `pyproject.toml`: プロジェクトの設定と依存関係を定義
- `uv.lock`: 具体的なバージョンを固定した依存関係ファイル
- 自動仮想環境管理: プロジェクトごとに独立した環境を自動作成

### コード品質ツール

#### Ruff

**機能**: Python向けの高速なリンター・フォーマッター

- コードスタイルの統一（PEP 8準拠）
- 潜在的なバグやコード品質の問題を検出
- 自動コード整形機能

**使用方法**:

```sh
# リンターの実行（問題の検出）
uv run --frozen ruff check

# フォーマッターの実行（コードの自動整形）
uv run --frozen ruff format

# 自動修正可能な問題の修正
uv run --frozen ruff check --fix --show-fixes --exit-non-zero-on-fix
```

#### Pyright

**機能**: Microsoft製のPython静的型チェッカー

- 型注釈に基づく型チェック
- 未定義変数や関数の検出
- VS Codeとの高い親和性

**使用方法**:

```sh
# 型チェックの実行
uv run --frozen pyright

# 特定ファイルの型チェック
uv run --frozen pyright template_cli_python/cli.py
```

#### pytest/coverage

**機能**: Python向けのテスティングフレームワーク

- 単体テストの実行
- テストの自動発見機能
- アサーション機能の提供
- テスト実行時のコードカバレッジ計測・レポート生成
- 未テストコードの可視化

**使用方法**:

```sh
# 全テストの実行
uv run --frozen pytest

# 特定のテストファイルを実行
uv run --frozen pytest tests/test_arithmetic_ops.py

# 詳細な出力でテスト実行
uv run --frozen pytest -v

# カバレッジレポート出力
uv run --frozen pytest --cov=template_cli_python --cov-report=term
```

### 開発支援ツール

#### taskipy

**機能**: Python用のタスクランナー

- 複雑なコマンドの簡略化
- 開発フローの自動化
- 複数コマンドの組み合わせ実行
- 実装したアプリケーションの動作確認にも利用可能

**設定例** (`pyproject.toml`に以下のような設定を追加)：

```toml
[tool.taskipy.tasks]
format = { cmd = "uv run --frozen ruff format", help = "run format" }
lint = { cmd = "uv run --frozen ruff check --fix --show-fixes --exit-non-zero-on-fix", help = "run lint" }
typecheck = { cmd = "uv run --frozen pyright", help = "run typecheck" }
test = { cmd = "uv run --frozen pytest --cov=src --cov-report=term", help = "run pytest with coverage report" }
check = { cmd ="task format && task lint && task typecheck", help = "run format, lint, typecheck" }
```

**使用方法**:

```sh
# 個別タスクの実行
uv run task format
uv run task lint
uv run task typecheck
uv run task test

# 全チェックの一括実行
uv run task check
```

#### Commitizen

**機能**: 統一されたコミットメッセージ形式とバージョン管理

- [Conventional Commits](https://www.conventionalcommits.org/)形式の強制
- セマンティックバージョニングによる自動バージョン管理
- CHANGELOGの自動生成

**使用方法**:

```sh
# インタラクティブなコミット（推奨）
uv run --frozen cz commit

# 短縮形
uv run --frozen cz c

# バージョンアップとタグ作成
uv run --frozen cz bump

# CHANGELOGの生成
uv run --frozen cz changelog --incremental
```

**コミットメッセージの形式**:

Commitizenは[Conventional Commits](https://www.conventionalcommits.org/)形式を強制します。基本的な形式は以下の通りです：

```text
<type>(<scope>): <description>
```

**主要なtype**:

- `feat`: 新機能の追加（ユーザー向けの新機能、ビルドスクリプトの新機能ではない）
- `fix`: バグ修正（ユーザー向けのバグ修正、ビルドスクリプトの修正ではない）
- `docs`: ドキュメントのみの変更
- `style`: コードの動作に影響しない変更（フォーマット、セミコロンの欠落など、本番コードの変更なし）
- `refactor`: 本番コードのリファクタリング（例：変数名の変更、バグ修正でも機能追加でもない）
- `test`: 不足していたテストの追加や既存テストの修正（本番コードの変更なし）
- `chore`: uv buildやmakeタスクの更新など（本番コードの変更なし、依存関係の更新、ビルドツールの変更）


**実例**:

- ワンラインコメント

    ```text
    feat(cli): データ処理用のサブコマンドを追加
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

> **詳細なガイドライン**: より詳しいコミットメッセージの作成方法については、[development-guidelines.md](./development-guidelines.md#コミットメッセージ) を参照してください。

## ツール自動化の設定

開発ツールは以下の3つの方法で自動実行されます：

1. **VS Code統合**: エディタでリアルタイムに実行
2. **pre-commit hooks**: コミット時に自動実行
3. **Nox**: 明示的なコマンド実行

### VS Code統合

これらのPython開発ツールは`.vscode/settings.json`でVS Codeと統合されており、以下の機能が自動的に動作します：

#### 自動実行される機能

- **Pyright**: ファイル編集中にリアルタイムで型チェックを実行
- **Ruff**: 保存時に自動フォーマットとリンターチェックを実行
- **エラー表示**: 問題パネルでruffとpyrightの警告・エラーを確認可能

#### 設定の有効化

VS Codeの設定はプロジェクトルートの`.vscode`フォルダに直接含まれており、追加のコピーやリンク作業は不要です。

### pre-commitによる自動チェック

コミット時に自動的にコード品質チェックを実行するため、pre-commitが設定されています。

#### 実行されるチェック

コミット時に以下が自動実行されます：

- **Ruff check**: コードスタイルと品質チェック（自動修正付き）
- **Ruff format**: コードフォーマット
- **Pyright**: 静的型チェック
- **pytest**: テスト実行
- **Commitizen**: コミットメッセージの形式チェック

#### 導入方法

`.pre-commit-config.yaml`をプロジェクトのルートディレクトリに配置して、次のコマンドを実行します。

```sh
pre-commit install
```

#### 手動実行

全ファイルに対してpre-commitチェックを実行する場合：

```sh
uv run pre-commit run --all-files
```

### Noxによる明示的実行

`Nox`を使用して、CI/CD環境と同じ条件で開発ツールを明示的に実行できます。

#### 利用可能なセッション

```sh
# リンターの実行（ruff check + format）
uv run nox -s lint

# 型チェックの実行（pyright）
uv run nox -s pyright

# テストの実行（pytest + coverage）
uv run nox -s coverage

# 全セッションの実行
uv run nox
```

#### 各セッションの詳細

- **lint**: Ruffによるコードスタイルチェックとフォーマット
- **pyright**: Pyrightによる静的型チェック
- **coverage**: pytestによるテスト実行とカバレッジ計測

## 環境設定の自動化

開発環境毎に環境変数を変更するためのツールである`direnv`と`mise`の使い方を説明します。`direnv`は環境変数の
自動化ツールとして有名であり、LinuxだけでなくWindowsでも利用できます。`mise`はより後発のツールであり、
環境変数の自動設定以外にも多言語のツール管理とタスクランナーの機能を持っています。
ただし、こちらはGit Bash for WindowsのようなWindows上のBashでの動作には不具合があります。

### direnvの設定

`direnv`の導入方法を説明します。Windows環境で利用する場合はこちらをおすすめします。

#### Linuxの場合

以下のコマンドでインストールします。

```sh
curl -sfL https://direnv.net/install.sh | bash
```

もし、インストール後のメッセージに記載されたインストール先にパスが通っていない場合はパスを通してください。環境によってインストール先は異なりますが、`$HOME/.cargo/bin`のようなディレクトリにインストールされるはずです。

加えて、`direnv`を有効化するために以下を`.bashrc`などの設定ファイルに記載してください。

```sh
eval "$(direnv hook bash)"
```

#### Git Bash for Windowsの場合

<https://github.com/direnv/direnv/releases> から`direnv.windows-amd64`のようなリンクからWindows用実行ファイルをダウンロードして、パスの通ったディレクトリに配置してください。例えば、`$HOME/.local/bin/direnv.windows-amd64.exe`に配置した場合、`.bashrc`に次のような設定を記載します。

```sh
alias direnv="$HOME/.local/bin/direnv.windows-amd64.exe"
eval "$(direnv hook bash)"
```

#### direnvの使用例

利用者の環境によって設定すべき環境変数は異なるため、このプロジェクトではdirenvの設定ファイルはプロジェクトルートには配置しておらず、配置して利用した場合も`.gitignore`により管理対象から外すようにしています。

基本的な設定は共通ですので最低限の設定内容を`context/`以下に準備しています。これを利用する場合は以下のように`context/_envrc`をプロジェクトルートにコピーするか、シンボリックリンクを作成してください。

```sh
git clone https://github.com/mkiyooka/template_cli_python.git && cd template_cli_python
cp context/_envrc .envrc
# シンボリックリンクを利用する場合は以下のコマンドを利用してください。
# ln -s context/_envrc .envrc
direnv allow
```

### miseの設定

続いて`mise`を利用した自動化について説明します。`mise`が生成するパスはGit for WindowsなどのBashには対応していないため、Windowsでは`direnv`の利用をおすすめします。ただし、開発ツール管理やタスクランナー機能も持っているためLinux上での開発がメインとなる場合はこちらがおすすめです。

`mise`は以下のコマンドでインストールできます。

```sh
curl https://mise.run | sh
```

続いて、コンソールへの出力内容にしたがって、`.bashrc`等に設定を追加してください。
`bash`の場合は以下のようなコマンドを実行すれば、設定できます。

```sh
echo "eval \"\$($HOME/.local/bin/mise activate bash)\"" >> "$HOME/.bashrc"
```

#### miseの使用例

`direnv`の項に記載したように利用者の環境によって設定すべき環境変数は異なるため、このプロジェクトではmiseの設定ファイルもプロジェクトルートには配置しておらず、配置して利用した場合も`.gitignore`により管理対象から外すようにしています。

基本的な設定は共通ですので最低限の設定内容を`context/`以下に準備しています。これを利用する場合は以下のように`context/mise.toml`をプロジェクトルートにコピーするか、シンボリックリンクを作成してください。

```sh
git clone https://github.com/mkiyooka/template_cli_python.git && cd template_cli_python
cp context/mise.toml ./
# シンボリックリンクを利用する場合は以下のコマンドを利用してください。
# ln -s context/mise.toml mise.toml
mise trust
```

---

## ツール間の詳細な呼び出し経路と設定ファイルの役割

### 詳細な呼び出し経路

| 実行方法 | 具体的なコマンド例 | 呼び出される実行ツール |
|:---|:---|:---|
| **VS Code (extension)** | 自動実行（設定依存） | Ruff, Pyright |
| **VS Code (test機能)** | テストエクスプローラー | pytest |
| **git commit** | `git commit` → pre-commit hooks | Ruff, Pyright, pytest, Commitizen |
| **uv run 直接** | `uv run --frozen ruff check` | Ruff |
| | `uv run --frozen pyright` | Pyright |
| | `uv run --frozen pytest --cov=src` | pytest |
| | `uv run --frozen cz commit` | Commitizen |
| **taskipy経由** | `uv run task format` | Ruff format |
| | `uv run task lint` | Ruff check |
| | `uv run task typecheck` | Pyright |
| | `uv run task test` | pytest --cov |
| | `uv run task check` | Ruff + Pyright (複合) |
| **nox経由** | `uv run nox -s lint` | Ruff check + format |
| | `uv run nox -s pyright` | Pyright |
| | `uv run nox -s coverage` | pytest --cov |
| | `uv run nox` | 全セッション実行 |

### 利用例まとめ

- **VS Code**: 拡張機能（extension）経由で`Ruff`や`Pyright`が自動実行され、保存時や編集時に品質・型チェックが可能。テスト機能からも`pytest`を実行可能。
- **pre-commit**: `git commit`時に`Ruff`、`Pyright`、`pytest`、`Commitizen`が自動実行され、コミット前に品質・型安全性・テスト・メッセージ形式を強制。
- **uv run**: `uv run`コマンドの下で`uv run --frozen ruff/pyright/pytest/commitizen`など個別に実行可能。
- **taskipy**: `uv run task check`で`task format`、`task lint`、`task typecheck`、`task test`など複数のタスク（taskipyタスク）が順次呼び出される。
- **Nox**: `uv run nox`の1コマンドで、リント・型チェック・テストが全て自動で実行される。

### 設定ファイルの役割

各設定ファイルがどのツールと連携し、どのタイミングで使用されるかを以下の表で示します：

| 設定ファイル | 対応ツール | 役割 | 実行タイミング |
|:---|:---|:---|:---|
| `pyproject.toml` [project] | uv | プロジェクト基本情報・依存関係定義 | `uv sync`, `uv add` 実行時 |
| `.pre-commit-config.yaml` | pre-commit | コミット時の自動チェック | `git commit` 実行時 |
| `pyproject.toml` [tool.taskipy.tasks] | taskipy | 開発タスクの簡略化 | `uv run task <タスク名>` 実行時 |
| `pyproject.toml` [tool.ruff.*] | Ruff | Ruffの動作設定（リント・フォーマットルール） | Ruff実行時の全場面 |
| `pyproject.toml` [tool.pyright] | Pyright | Pyrightの動作設定（型チェック設定） | Pyright実行時の全場面 |
| `pyproject.toml` [tool.pytest.*] | pytest | pytestの実行設定（テスト発見・実行オプション） | pytest実行時 |
| `pyproject.toml` [tool.coverage.*] | coverage | カバレッジ計測設定 | coverage/pytest実行時 |
| `pyproject.toml` [tool.commitizen] | Commitizen | バージョン管理・CHANGELOG生成設定 | `cz bump`, `cz changelog` 実行時 |
| `noxfile.py` | Nox | CI/CD用の隔離実行環境 | `uv run nox` 実行時 |
| `.vscode/settings.json` | VS Code (Ruff, Pyright) | VS Code統合設定 | VS Code使用時 |

#### ツール別設定ファイル対応

- **Ruff**: `pyproject.toml` [tool.ruff.*], `.vscode/settings.json`, `.pre-commit-config.yaml`
- **Pyright**: `pyproject.toml` [tool.pyright], `.vscode/settings.json`, `.pre-commit-config.yaml`
- **pytest**: `pyproject.toml` [tool.pytest.*], `.pre-commit-config.yaml`
- **coverage**: `pyproject.toml` [tool.coverage.*]
- **Commitizen**: `pyproject.toml` [tool.commitizen], `.pre-commit-config.yaml`
- **taskipy**: `pyproject.toml` [tool.taskipy.tasks]
- **Nox**: `noxfile.py`
