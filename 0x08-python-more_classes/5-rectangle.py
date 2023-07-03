#!/usr/bin/python3
"""Module 5-rectangle
Rectangle class Definition.
"""


class Rectangle:
    """ definition of Rectangle class using width and height."""

    def __init__(self, width=0, height=0):
        """Rectangle instance initialization.

        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns Rectangle instance string representation
        using '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for a in range(self.__height):
            for b in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Return Rectangle instance string representation
        This uses eval() to recreate new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Rectangle instance deletion."""
        print("Bye rectangle...")

    @property
    def width(self):
        """gets Rectangle instance width."""
        return self.__width

    @width.setter
    def width(self, value):
        """declares Rectangle instance width

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
        """gets Rectangle instance height."""
        return self.__height

    @height.setter
    def height(self, value):
        """declares a Rectangle instance height

        Args:
            value: positive integer height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculation of Rectangle instance area

        Returns:
            the rectangle Area = height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculation of Rectangle instance perimeter

        Returns:
            the rectangle Perimeter = 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
