#!/usr/bin/python3
"""module for returning Python to JSON."""


def class_to_json(obj):
    """Returns simple data structure dictionary."""
    return obj.__dict__
