#!/usr/bin/python3
"""Module 4-rectangle
Rectangle class definition.
"""


class Rectangle:
    """defines Rectangle class using width & height."""

    def __init__(self, width=0, height=0):
        """Rectangle instance initialization.

        Args:
            width: the rectangle width
            height: the rectangle height
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns a Rectangle instance string representation
        using the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for a in range(self.__height):
            for b in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Returns a Rectangle instance with string representation
        This can use eval() to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """gets Rectangle width of an instance """
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
        """gets the Rectangle instance height."""
        return self.__height

    @height.setter
    def height(self, value):
        """declares Rectangle instance height

        Args:
            value: positive integer height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the Rectangle instance area

        Returns:
            the rectangle Area = height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Rectangle instance perimeter Calculator

        Returns:
            The rectangle Perimeter = 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
