# type: ignore

import nox


def tests(session):
    session.install(".[dev]")
    session.run("ruff", "format", "--diff")
    session.run("ruff", "check")
    session.run("pytest")
    session.run("mypy", "src")
