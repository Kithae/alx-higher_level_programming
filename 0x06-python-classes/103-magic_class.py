#!/usr/bin/python3
"""Magic class from a given ByteCode."""
import math

class MagicClass:
    """ MagicClass Initialization."""
    def __init__(self, radius=0):
        """ data Initialization."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """area Calculation."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """circumference Calculation."""
        return 2 * math.pi * self._MagicClass__radius
