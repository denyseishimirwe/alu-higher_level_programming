#!/usr/bin/python3

# Import the 'add' function from add_0.py
from add_0 import add

if __name__ == "__main__":
    # Define variables
    a = 1
    b = 2

    # Call the add function and print the result using string format
    print("{} + {} = {}".format(a, b, add(a, b)))
