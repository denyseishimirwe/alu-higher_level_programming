#!/usr/bin/python3


"""
This module defines a Square class that represents a square shape with a private size attribute.
It includes methods for object instantiation and controlled access to the size attribute.
"""


class Square:
    """
    A Square class that defines a square with a private size attribute.
    
    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with a specified size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square object, showing its size.
        
        Returns:
            str: A string representation of the square with its size.
        """
        return f"Square(size={self.__size})"

if __name__ == "__main__":
    # Test with a square of size 3
    my_square = Square(3)
    print(type(my_square))  # Should print the type of the object (Square)
    print(my_square.__dict__)  # Should print the internal dictionary with private size
    
    # Test with another square of size 89
    another_square = Square(89)
    print(type(another_square))  # Should print the type of the object (Square)
    print(another_square.__dict__)  # Should print the internal dictionary with private size
    
    # Try accessing the 'size' attribute (it should fail as it is private)
    try:
        print(my_square.size)
    except Exception as e:
        print(e)  # Should print the exception message

    # Try accessing the '_size' attribute (it should fail as it is private and mangled)
    try:
        print(my_square._size)
    except Exception as e:
        print(e)  # Should print the exception message
