"""
Entrypoints module

Main console script entrypoints for the do_cli tool
"""
import sys

from cli import DOCLI

MIN_VERSION = (3, 6)
RUNTIME_VERSION = (sys.version_info.major, sys.version_info.minor)

if RUNTIME_VERSION < MIN_VERSION:
    sys.exit('Error: compose-flow runs on Python3.6+')


def do_cli():
    """
    Main entrypoint
    """

    response = DOCLI().run()

    sys.exit(response)
