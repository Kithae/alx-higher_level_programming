#!/usr/bin/python3
"""module for reading a JSON file."""
import json


def load_from_json_file(filename):
    """Creates from a JSON file Python objects."""
    with open(filename) as f:
        return json.load(f)
