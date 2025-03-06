#!/usr/bin/python3
def no_c(my_string):
    # Create a new string by removing 'c' and 'C' from the original string
    return "".join([char for char in my_string if char not in ['c', 'C']])
