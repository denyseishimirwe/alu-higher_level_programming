#!/usr/bin/python3

"""
Module that defines a Square class.

The Square class is initialized with a size and has methods to:
1. Retrieve and set the size of the square with validation.
2. Calculate the area of the square.
3. Print the square using the '#' character.
"""

class Square:
    """Square class that defines a square by its size and can print it"""
    
    def __init__(self, size=0):
        """Initializes the square with a size, defaults to 0"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
                """Print the square with '#' or an empty line if size is 0"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
