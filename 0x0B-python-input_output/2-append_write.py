#!/usr/bin/python3
"""module for appending files."""


def append_write(filename="", text=""):
    """Appends string to UTF8 text file end.

    Args:
        filename (str): file name.
        text (str): string.
    Returns:
        Total appended characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
