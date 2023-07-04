#!/usr/bin/python3
"""Module max_integer
"""


def max_integer(list=[]):
    """Finds maximum integer in the list
        Returns none for an empty list
    """
    if len(list) == 0:
        return None
    result = list[0]
    a = 1
    while a < len(list):
        if list[a] > result:
            result = list[a]
        a += 1
    return result
