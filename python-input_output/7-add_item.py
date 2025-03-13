#!/usr/bin/python3


"""
Script that adds all arguments to a Python list, and then saves them to a file.
"""

from sys import argv
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list or initialize an empty one
current_list = load_from_json_file(filename) if not FileNotFoundError else []

# Add all arguments (except the script name) to the list
current_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(current_list, filename)
