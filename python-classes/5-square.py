#!/usr/bin/python3


"""
Defines a Square class with size validation and area calculation.
"""


class Square:
    """Class representing a square with size validation, getter, and setter."""

    def __init__(self, size=0):
        """Initialize the square with an optional size (default is 0)."""
        self.size = size  # This will call the setter

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to calculate the area of the square."""
        return self.__size ** 2

    def display(self):
        """Method to print the square's size and area."""
        print("Size: {}, Area: {}".format(self.size, self.area()))


if __name__ == "__main__":
    my_square = Square(89)
    my_square.display()

    my_square.size = 3
    my_square.display()

    try:
        my_square.size = "5 feet"
        my_square.display()
    except Exception as e:
        print(e)
