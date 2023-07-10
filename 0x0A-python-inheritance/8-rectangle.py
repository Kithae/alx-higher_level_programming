#!/usr/bin/python3
"""inherited class Rectangle definition."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle Representation using BaseGeometry."""

    def __init__(self, width, height):
        """ new Rectangle initialization.

        Args:
            width (int): rect widt.
            height (int): rect height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
