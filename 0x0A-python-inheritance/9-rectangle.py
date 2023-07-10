#!/usr/bin/python3
"""class Rectangle definition."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle representation."""

    def __init__(self, width, height):
        """new Rectangle Intialization.

        Args:
            width (int): rect width.
            height (int): rect height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Returns Rectangle print() and str()."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
