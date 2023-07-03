#!/usr/bin/python3
"""Module 8-rectangle
Rectangle class definition.
"""


class Rectangle:
    """Rectangle class definition using width and height.

    Attributes:
        number_of_instances: total Rectangle increments instances,
        after every insertion and decrements after deletion
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Rectangle instance initialization.

        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns Rectangle instance string representation
        using '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for a in range(self.__height):
            for b in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Return Rectangle instance string representation
        This uses eval()to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Rectangle instance deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        """Calculate Rectangle instance area

        Returns:
            the rectangle Area = height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Rectangle instance perimeter calculation

        Returns:
            the rectangle Perimeter = 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """determines biggest Rectangle using area

        Args:
            rect_1: first Rectangle instance
            rect_2: second Rectangle instance

        Returns:
            The biggest area instance or,
            first rectangle if area is same
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
