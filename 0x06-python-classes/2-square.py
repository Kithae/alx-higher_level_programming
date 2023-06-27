#!/usr/bin/python3
"""
Define a class square.
"""


class Square:
    """
    A class definition of a square.
    """

    def __init__(self, size=0):
        """
        new Square initialization.

        Args:
            size (int): The square size.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
