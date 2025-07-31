# 開発者向けガイド

## uvの導入

このプロジェクトはパッケージ管理ツールとして`uv`を利用することを前提としています。以下の手順で`uv`をセットアップしてください。
これにより`uv`コマンドと`uvx`コマンドが利用できます。
`uvx`は`uv tool run`のエイリアスで、ツールをインストールせず実行できます。

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## uvの自動補完の設定

bashの場合

```sh
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc
```

zshの場合

```sh
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```

## プロジェクトのセットアップ

以下のコマンドで依存パッケージをインストールしてください。
`pre-commit`はコード品質維持のため、コミット前に自動でチェックや整形を行うツールです。
`pre-commit`を利用することでコード整形、lint、test等の実行を強制することができます。

```sh
git clone https://github.com/mkiyooka/template_cli_python.git
cd template_cli_python
uv sync --all-groups
source .venv/bin/activate
uvx pre-commit install
```

## 環境管理ツールの設定（オプション）

このプロジェクトでは、環境管理ツールの設定テンプレートを `context/` ディレクトリに提供しています。
お使いの環境管理ツールに応じて、必要な設定をコピーしてください。

> **事前準備**: direnvやmise自体の導入方法については、[development-guide-tools.md](./development-guide-tools.md) を参照してください。

### direnvを使用する場合

```sh
cp context/_envrc .envrc
direnv allow
```

### miseを使用する場合

```sh
cp context/mise.toml .mise.toml
# または
cp context/mise.toml mise.toml
```

> **注意**: direnvとmiseを同時に使用する場合は競合する可能性があります。
> どちらか一方の設定のみを有効化することをお勧めします。

### 編集可能な状態でのインストール

開発中に動作確認を行うためには、editable installを利用してください。
editable installを利用すると、開発中のコード変更を即座に反映できます。
ただし、開発環境では依存関係の競合や不要なパッケージ混入を防ぐため`uv add`のみを利用します。
そのため、`uv pip`は開発環境とは異なる動作確認用ディレクトリを用意して、そのディレクトリで実行します。

```sh
git clone https://github.com/mkiyooka/template_cli_python.git template_cli_python
mkdir installcheck && cd installcheck
uv pip install -e ../template_cli_python
```

アンインストール方法は以下の通りですが、`uv pip uninstall`コマンドでは依存ライブラリ（このパッケージがインストール時に一緒に導入したパッケージ）が自動的に削除されず、環境内に残る場合があります。
特に他のプロジェクトでも同じ依存ライブラリを利用していない場合や、クリーンな環境を保ちたい場合は、手動で不要なパッケージを削除することをおすすめします。
手動で依存ライブラリを削除するには、`uv pip uninstall <パッケージ名>`を個別に実行してください。
また、不要なパッケージが多い場合や環境をリセットしたい場合は、仮想環境ごと削除して再作成するのが確実です。

```sh
uv pip uninstall template-cli-python
cd .. && rm -rf installcheck
```
