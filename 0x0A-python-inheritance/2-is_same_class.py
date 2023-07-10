#!/usr/bin/python3
"""module for checking a class."""


def is_same_class(obj, a_class):
    """a function that confirms objects as a given class instance.

    Args:
        obj (any): an object.
        a_class (type): a class.
    Returns:
        True else, False.
    """
    if type(obj) == a_class:
        return True
    return False
