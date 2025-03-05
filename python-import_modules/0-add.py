#!/usr/bin/python3

from add_0 import add  # Import the function (using add_0 only once)

a = 1  # Assigning value to 'a'
b = 2  # Assigning value to 'b'

# Single print function with string formatting
print("{} + {} = {}".format(a, b, add(a, b)))

