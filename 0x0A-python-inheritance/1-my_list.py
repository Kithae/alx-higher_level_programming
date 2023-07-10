#!/usr/bin/python3
"""A module to inherit from list class"""


class MyList(list):
    """the inheriting class (from list)"""
    def print_sorted(self):
        """printing sorted lists"""
        print(sorted(self))
