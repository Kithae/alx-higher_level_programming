#!/usr/bin/python3
"""module for string to JSON."""
import json


def to_json_string(my_obj):
    """Returns JSON representation."""
    return json.dumps(my_obj)
