#!/usr/bin/python3
"""text file reader."""


def read_file(filename=""):
    """Print UTF8 text file contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
