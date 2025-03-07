#!/usr/bin/python3


"""
Module to define a Square class with size validation and area computation.
"""


class Square:
    """Class representing a square with size validation and area calculation."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method to calculate the area of the square."""
        return self.__size ** 2


if __name__ == "__main__":
    for val in [3, 0, "3", -89]:
        try:
            sq = Square(val)
            print("Area: {}".format(sq.area()))
        except Exception as e:
            print(e)
