#!/usr/bin/python3


"""
This script adds command-line arguments to a Python list and saves it.
The list is stored in a JSON representation in a file named "add_item.json".

Functions:
    - Saves list to a file using save_to_json_file from 5-save_to_json_file.py.
    - Loads list using load_from_json_file from 6-load_from_json_file.py.

If the file does not exist, it will be created with an empty list.
"""

import sys
import os

# Importing save and load functions from external modules
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing data if the file exists, otherwise start with an empty list
if os.path.isfile(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments to the list (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(items, filename)
