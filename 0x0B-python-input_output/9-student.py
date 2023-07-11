#!/usr/bin/python3
"""module for student class."""


class Student:
    """student representation."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student.

        Args:
            first_name (str): student first name.
            last_name (str): student last name.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """student dictionary representation."""
        return self.__dict__
