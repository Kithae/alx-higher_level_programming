#!/usr/bin/python3
"""module for checking class and inherited classes."""


def is_kind_of_class(obj, a_class):
    """function for checking if object is a class or inherited instance.

    Args:
        obj (any): an object.
        a_class (type): a class
    Returns:
        True else, false.
    """
    if isinstance(obj, a_class):
        return True
    return False
