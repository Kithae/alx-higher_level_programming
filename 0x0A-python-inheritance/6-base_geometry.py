#!/usr/bin/python3
""" class definition of a BaseGeometry ."""


class BaseGeometry:
    """ base geometry Representation."""

    def area(self):
        """Not true."""
        raise Exception("area() is not implemented")
