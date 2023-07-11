#!/usr/bin/python3
"""module for inserting text file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after specific string in a file.

    Args:
        filename (str): a name.
        search_string (str): a string.
        new_string (str): new string.
    """
    ntext = ""
    with open(filename) as r:
        for line in r:
            ntext += line
            if search_string in line:
                ntext += new_string
    with open(filename, "w") as w:
        w.write(ntext)
