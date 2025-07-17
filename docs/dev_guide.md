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

## miseを利用した仮想環境を自動有効化

仮想環境を利用するための`source .venv/bin/activate`を省略するには、`mise`を導入してください。
`mise`は大きく3つの機能を提供します。

1. 開発ツールの管理
    : asdf, aquaのようにツールのバージョン管理ができます。バックエンドとしてnpm, pipx, cargoなどをサポートしており、幅広いツールを管理できます。
2. 仮想環境の設定の自動化
    : direnv, dotenvのように開発用ディレクトリ以下に移動すると、自動で設定ファイルを読み取り環境設定を自動的に実行できます。また、開発用ディレクトリ外に移動したときに自動的に設定を破棄できます。
3. タスクランナー
    : makeやTaskなどのように設定ファイルにあらかじめコマンドを登録しておくとtaskとして簡単に実行することができます。

```sh
curl https://mise.run | sh
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

アンインストール方法は以下の通りですが、依存ライブラが削除されず残るはずです。
必要に応じて環境全体を削除してください。

```sh
uv pip uninstall template-cli-python
cd .. && rm -rf installcheck
```
