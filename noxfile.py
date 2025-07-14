import nox

nox.options.default_venv_backend = "uv"


@nox.session(python=["3.13"], tags=["lint"])
def lint(session) -> None:
    session.install(".")
    session.install("ruff")
    session.run("ruff", "check", "--fix", "--show-fixes", "--exit-non-zero-on-fix", ".")
    session.run("ruff", "format", ".")


@nox.session(python=["3.13"], tags=["type"])
def pyright(session) -> None:
    session.install(".")
    session.install("pyright")
    session.run("pyright")


@nox.session(python=["3.13"], tags=["test"])
def coverage(session) -> None:
    session.install("-e", ".")
    session.install("pytest", "pytest-cov")
    session.run("pytest", "--cov=src", "--cov-report=xml", "--cov-report=term")
