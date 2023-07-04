#!/usr/bin/python3
"""
Module print_square
Printing # character square.
"""


def print_square(size):
    """Printing squares defined by width and length
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        for b in range(size):
            print('#', end='')
        print()
