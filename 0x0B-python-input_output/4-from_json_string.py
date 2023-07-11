#!/usr/bin/python3
"""module for JSON to object."""
import json


def from_json_string(my_str):
    """Returns Python equivalent of JSON string."""
    return json.loads(my_str)
