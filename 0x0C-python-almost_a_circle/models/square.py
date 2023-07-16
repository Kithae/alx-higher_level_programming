#!/usr/bin/python3
"""a class Square definition
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square representation Module
"""

    def __init__(self, size, x=0, y=0, id=None):
        """square Initialization
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """module to get Square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """module to set Square size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """module to represent square string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """module for square updating
        """
        if len(args):
            for a, arg in enumerate(args):
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """return a dictonary
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
