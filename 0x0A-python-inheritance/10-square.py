#!/usr/bin/python3
"""Rectangle sub-class Square definition."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square representation."""

    def __init__(self, size):
        """ new square Initialization.

        Args:
            size (int): square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
