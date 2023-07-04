#!/usr/bin/python3
"""
Module text_indentation
Adding new lines after specific characters.
"""


def text_indentation(text):
    """Printing text after {'.', '?', ':'} characters
    Followed by two new lines.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for dlm in ".:?":
        text = (dlm + "\n\n").join(
            [line.strip(" ") for line in text.split(dlm)])

    print("{}".format(text), end="")
