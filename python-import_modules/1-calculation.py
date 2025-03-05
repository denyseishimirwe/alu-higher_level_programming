#!/usr/bin/python3

from calculator_1 import add, sub, mul, div  # Import functions

a = 10  # Define variable a
b = 5   # Define variable b

if __name__ == "__main__":  # Ensure code runs only when executed directly
    print("{} + {} = {}".format(a, b, add(a, b)))  # Addition
    print("{} - {} = {}".format(a, b, sub(a, b)))  # Subtraction
    print("{} * {} = {}".format(a, b, mul(a, b)))  # Multiplication
    print("{} / {} = {}".format(a, b, div(a, b)))  # Division
