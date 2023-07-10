#!/usr/bin/python3
"""Rectangle definition of a sub-class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square representation."""

    def __init__(self, size):
        """ new square initialization.

        Args:
            size (int): sqr size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
