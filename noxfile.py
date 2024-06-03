import nox


@nox.session(python=["3.11", "3.12"])
def tests(session):
    session.install(".[dev]")
    session.run("ruff", "format", "--diff")
    session.run("ruff", "check")
    session.run("mypy", "src")
    session.run("pytest")
