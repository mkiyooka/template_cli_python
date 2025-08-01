# 開発用ツールの導入

このドキュメントでは、Python開発プロジェクトで使用する以下のツールの導入方法を説明します：

- **環境変数の自動化**
  - 環境変数管理: `direnv`
  - 環境変数管理/多言語ツール管理: `mise`
- **Pythonコードの品質とテストの自動化**
  - コード整形: `ruff`
  - リント: `ruff`
  - 静的型チェック: `pyright`
  - テストフレームワーク: `pytest`
  - タスクランナー: `taskipy`
  - コミット管理: `commitizen`

## 環境設定の自動化

開発環境毎に環境変数を変更するためのツールである`direnv`と`mise`の使い方を説明します。`direnv`は環境変数の自動化ツールとして有名であり、LinuxだけでなくWindowsでも利用できます。`mise`はより後発のツールであり、環境変数の自動設定以外にも多言語のツール管理とタスクランナーの機能を持っています。ただし、こちらはGit Bash for WindowsのようなWindows上のBashでの動作には不具合があります。

### direnvの設定

`direnv`の導入方法を説明します。Windows環境で利用する場合はこちらをおすすめします。

**Linuxの場合**

以下のコマンドでインストールします。

``` sh
curl -sfL https://direnv.net/install.sh | bash
```

もし、インストール後のメッセージに記載されたインストール先にパスが通っていない場合はパスを通してください。環境によってインストール先は異なりますが、`$HOME/.cargo/bin`のようなディレクトリにインストールされるはずです。

加えて、`direnv`を有効化するために以下を`.bashrc`などの設定ファイルに記載してください。

``` sh
eval "$(direnv hook bash)"
```

**Git Bash for Windowsの場合**

https://github.com/direnv/direnv/releases から`direnv.windows-amd64`のようなリンクからWindows用実行ファイルをダウンロードして、パスの通ったディレクトリに配置してください。例えば、`$HOME/.local/bin/direnv.windows-amd64.exe`に配置した場合、`.bashrc`に次のような設定を記載します。

``` sh
alias direnv="$HOME/.local/bin/direnv.windows-amd64.exe"
eval "$(direnv hook bash)"
```

**このプロジェクトでの使用例**
ただし、基本的な設定は共通ですので最低限の設定内容を`context/`以下に準備しています。これを利用する場合は以下のように`context/_envrc`をプロジェクトルートにコピーするか、シンボリックリンクを作成してください。
利用者の環境によって設定すべき環境変数は異なるため、このプロジェクトではmiseやdirenvの設定ファイルはプロジェクトルートには配置しておらず、配置して利用した場合も`.gitignore`により管理対象から外すようにしています。
ただし、基本的な設定は共通ですので最低限の設定内容を`context/`以下に準備しています。これを利用する場合は以下のように`context/_envrc`をプロジェクトルートにコピーするか、シンボリックリンクを作成してください。

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

``` sh
echo "eval \"\$($HOME/.local/bin/mise activate bash)\"" >> "$HOME/.bashrc"
```

**このプロジェクトでの使用例**
`mise`についても、基本的な設定は共通ですので最低限の設定内容を`context/`以下に準備しています。これを利用する場合は以下のように`context/mise.toml`をプロジェクトルートにコピーするか、シンボリックリンクを作成してください。
`direnv`の項に記載したように利用者の環境によって設定すべき環境変数は異なるため、このプロジェクトではmiseの設定ファイルもプロジェクトルートには配置しておらず、配置して利用した場合も`.gitignore`により管理対象から外すようにしています。
`mise`についても、基本的な設定は共通ですので最低限の設定内容を`context/`以下に準備しています。これを利用する場合は以下のように`context/mise.toml`をプロジェクトルートにコピーするか、シンボリックリンクを作成してください。

```sh
git clone https://github.com/mkiyooka/template_cli_python.git && cd template_cli_python
cp context/mise.toml ./
# シンボリックリンクを利用する場合は以下のコマンドを利用してください。
# ln -s context/mise.toml mise.toml
mise trust
```

## Python開発ツールの導入と設定

このプロジェクトでは、**Python開発**におけるコード品質の向上とテストの自動化のために複数の開発ツールを利用しています。これらのツールは`uv sync`コマンドで一括導入できるように`pyproject.toml`に設定されています。

開発ツールは以下の3つの方法で自動実行されます：
1. **VS Code統合**: エディタでリアルタイムに実行
2. **Pre-commit hooks**: コミット時に自動実行
3. **Nox**: 明示的なコマンド実行

### 一括導入方法

プロジェクトのセットアップ後、以下のコマンドを実行することで、開発に必要なすべてのツールが自動的にインストールされます：

```sh
# プロジェクトをクローン後、ディレクトリに移動
git clone https://github.com/mkiyooka/template_cli_python.git && cd template_cli_python

# 開発用ツールを含む全ての依存関係を一括インストール
uv sync

# または明示的に全グループを指定
uv sync --all-groups
```

`uv sync`は`pyproject.toml`に定義された`dev`グループの依存関係をインストールするため、個別にツールをインストールする必要がありません。

### 各ツールの機能と役割

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
uv run --frozen pyright src/template_cli_python/cli.py
```

#### Pytest

**機能**: Python向けのテスティングフレームワーク
- 単体テストの実行
- カバレッジレポートの生成
- テストの自動発見機能

**使用方法**:
```sh
# 全テストの実行
uv run --frozen pytest

# カバレッジ付きでテスト実行
uv run --frozen pytest --cov=src --cov-report=term

# 特定のテストファイルを実行
uv run --frozen pytest tests/test_arithmetic_ops.py
```

#### Taskipy

**機能**: Python用のタスクランナー
- 複雑なコマンドの簡略化
- 開発フローの自動化
- 複数コマンドの組み合わせ実行

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
uv run --frozen cz changelog
```

**コミットメッセージの形式**:
```
feat: 新機能の追加
fix: バグ修正
docs: ドキュメントの変更
style: コードフォーマットの変更
refactor: リファクタリング
test: テストの追加・修正
chore: その他の変更
```

### VS Codeとの統合

これらのPython開発ツールは`_vscode/settings.json`でVS Codeと統合されており、以下の機能が自動的に動作します：

#### 自動実行される機能
- **Pyright**: ファイル編集中にリアルタイムで型チェックを実行
- **Ruff**: 保存時に自動フォーマットとリンターチェックを実行
- **エラー表示**: 問題パネルでruffとpyrightの警告・エラーを確認可能

#### 設定の有効化
VS Code設定を有効化するには、プロジェクトルートの`_vscode`フォルダを`.vscode`にコピーまたはリンクしてください：

```sh
# コピーする場合
cp -r _vscode .vscode

# シンボリックリンクを作成する場合（推奨）
ln -s _vscode .vscode
```

### Pre-commitによる自動チェック

コミット時に自動的にコード品質チェックを実行するため、pre-commitが設定されています。

#### Pre-commitの初期設定
```sh
# pre-commitのインストール（uv syncで既にインストール済み）
# git hooksの設定
uv run pre-commit install
```

#### 実行されるチェック
コミット時に以下が自動実行されます：
- **Ruff check**: コードスタイルと品質チェック（自動修正付き）
- **Ruff format**: コードフォーマット
- **Commitizen**: コミットメッセージの形式チェック

#### 手動実行
全ファイルに対してpre-commitチェックを実行する場合：
```sh
uv run pre-commit run --all-files
```

### Noxによる明示的実行

`nox`を使用して、CI/CD環境と同じ条件で開発ツールを明示的に実行できます。

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
- **coverage**: Pytestによるテスト実行とカバレッジ計測
