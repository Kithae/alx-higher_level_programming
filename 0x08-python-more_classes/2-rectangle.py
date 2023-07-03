#!/usr/bin/python3
"""Module 2-rectangle
Rectangle class definition.
"""


class Rectangle:
    """the width and height Rectangle class definition."""

    def __init__(self, width=0, height=0):
        """Rectangle instance initialization.

        Args:
            width: the rectangle width
            height: the rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets Rectangle width instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """declares Rectangle width instance

        Args:
            value: positive integer width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets Rectangle height instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """declares Rectangle height instance

        Args:
            value: positive integer height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Rectangle area calculation of an instance

        Returns:
            The area = height x width
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Rectangle perimeter calculation of an instance

        Returns:
            The rectangle perimeter = 2 x (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
