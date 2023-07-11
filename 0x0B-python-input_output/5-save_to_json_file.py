#!/usr/bin/python3
"""module to write JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes using JSON representation to a text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
