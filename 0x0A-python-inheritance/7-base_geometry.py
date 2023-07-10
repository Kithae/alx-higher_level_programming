#!/usr/bin/python3
""" class definition of a BaseGeometry."""


class BaseGeometry:
    """ base geometry Representation. """

    def area(self):
        """Not true."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integers.

        Args:
            name (str): parameter name.
            value (int): parameter value.
        Raises:
            TypeError: for non-integer.
            ValueError: value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
