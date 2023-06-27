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
        self.size = size

    @property
    def size(self):
        """get size property"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """print area of the current square"""
        return (self.__size * self.__size)
