#!/usr/bin/python3
"""Module 1-rectangle
A Rectangle class definition.
"""


class Rectangle:
    """Rectangle class definition using width & height."""

    def __init__(self, width=0, height=0):
        """ Rectangle instance initialized.

        Args:
            width: the rectangle width
            height: the rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the rectangle width instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """declares the rectangle width instance

        Args:
            value: a positive integer width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the rectangle height instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """declares the rectangle height instance

        Args:
            value: a positive integer height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
