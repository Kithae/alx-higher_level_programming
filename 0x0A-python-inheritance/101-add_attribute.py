#!/usr/bin/python3
"""module for adding object attributes."""


def add_attribute(obj, att, value):
    """Addition of new object attributes.

    Args:
        obj (any): an object.
        att (str): attribute name.
        value (any): attribute value.
    Raises:
        TypeError: impossible to add the attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
