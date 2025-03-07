#!/usr/bin/python3


"""
Module to define a Square class with size validation.
"""

class Square:
    """Class representing a square with size validation."""
    def __init__(self, size=0):
        if not isinstance(size, int): raise TypeError("size must be an integer")
        if size < 0: raise ValueError("size must be >= 0")
        self.__size = size

if __name__ == "__main__":
    for val in [3, 0, "3", -89]:
        try: sq = Square(val)
        except Exception as e: print(e)
