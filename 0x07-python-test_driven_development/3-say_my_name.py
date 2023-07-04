#!/usr/bin/python3
"""
Module say_my_name
Printing first and last names as given.
"""


def say_my_name(first_name, last_name=""):
    """Prints <last_name> and <first_name> string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
