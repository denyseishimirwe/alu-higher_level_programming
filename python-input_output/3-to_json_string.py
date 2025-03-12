#!/usr/bin/python3


import json
"""
Module to convert Python objects to JSON strings.

This module contains a function `to_json_string` that serializes Python
objects into JSON strings. If the object cannot be serialized, an error
message is returned indicating the type of error encountered.

Usage:
    - `to_json_string(my_obj)` - Converts a Python object `my_obj` into its
      JSON string representation.
"""


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON string representation.
    Args:
        my_obj: The Python object to be serialized into a JSON string.    
    Returns:
        A JSON string representation of the input object. If the object
        cannot be serialized, returns an error message in the format
        '[ErrorType] error_message'.
    """
    try:
        return json.dumps(my_obj)
    except (TypeError, ValueError) as e:
        return f"[{e.__class__.__name__}] {e}"
