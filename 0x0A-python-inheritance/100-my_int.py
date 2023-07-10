#!/usr/bin/python3
""" MyInt class definition."""


class MyInt(int):
    """Inverts the integer operators == and !=."""

    def __eq__(self, value):
        """Overrides == opeartors using != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operators using == behavior."""
        return self.real == value
