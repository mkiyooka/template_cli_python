"""Command line interface entry point.

This module provides the entry point for running the CLI application
using `python -m <package_name>`.
"""

if __name__ == "__main__":
    from . import cli

    cli.app()
