#!/usr/bin/python3


class Square:


    """
    This class defines a square with a private size attribute.
    
    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square object.
        """
        return f"Square(size={self.__size})"

if __name__ == "__main__":
    # Create a Square instance with size 3
    my_square = Square(3)
    print(type(my_square))  # Output the type of the square object
    print(my_square.__dict__)  # Output the internal dictionary of the object

    # Create a Square instance with size 89
    another_square = Square(89)
    print(type(another_square))  # Output the type of the square object
    print(another_square.__dict__)  # Output the internal dictionary of the object

    # Try accessing the 'size' attribute (it should fail)
    try:
        print(my_square.size)
    except Exception as e:
        print(e)  # Print the exception message

    # Try accessing the '_size' attribute (it should fail)
    try:
        print(my_square._size)
    except Exception as e:
        print(e)  # Print the exception message
