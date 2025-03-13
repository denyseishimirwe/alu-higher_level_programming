#!/usr/bin/python3


"""
Script that adds all arguments to a Python list, and then saves them to a file.

This script uses the save_to_json_file and load_from_json_file functions
to load a list from a file, add new items (from command-line arguments),
and save the updated list back to the file.
"""

from sys import argv
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list or initialize an empty one
try:
    current_list = load_from_json_file(filename)
except FileNotFoundError:
    current_list = []

# Add all arguments (except the script name) to the list
current_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(current_list, filename)
