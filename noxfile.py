import nox

nox.options.default_venv_backend = "uv|virtualenv"


@nox.session(python=["3.10"], tags=["lint"])
def lint(session) -> None:
    session.install(".")
    session.install("ruff")
    session.run("ruff", "check", "--fix", "--show-fixes", "--exit-non-zero-on-fix", ".")
    session.run("ruff", "format", ".")
