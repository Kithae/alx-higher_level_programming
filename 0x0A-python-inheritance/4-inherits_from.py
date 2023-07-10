#!/usr/bin/python3
"""module for checking an inherited class."""


def inherits_from(obj, a_class):
    """a function to check if an object is inherited class instance.

    Args:
        obj (any): an object.
        a_class (type): a class.
    Returns:
        True else, False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
