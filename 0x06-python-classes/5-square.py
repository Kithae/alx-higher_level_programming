#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """a Square representation."""

    def __init__(self, size):
        """ new Square initialization.
        Args:
            size (int): The square size.
        """
        self.size = size

    @property
    def size(self):
        """Get current Square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """print area of current square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print #character square."""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
