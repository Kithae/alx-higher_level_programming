#!/usr/bin/python3
"""module for writing a file."""


def write_file(filename="", text=""):
    """Writing string to UTF8 text file.

    Args:
        filename (str): file name.
        text (str): string.
    Returns:
        Total written characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
