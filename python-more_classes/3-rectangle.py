#!/usr/bin/python3


"""
A class to represent a rectangle.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

Methods:
    area(): Returns the area of the rectangle.
    perimeter(): Returns the perimeter of the rectangle.
    __str__(): Returns a string representation of the rectangle as a grid of '#' characters.
    __repr__(): Returns a string that represents the rectangle object.
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
            If either width or height is 0, returns 0.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Returns a string representation of the rectangle as a grid of '#' characters.

        Returns:
            str: A string of '#' characters representing the rectangle.
            If width or height is 0, returns an empty string.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width] * self._height)

    def __repr__(self):
        """
        Returns a string that represents the rectangle object.

        Returns:
            str: The official string representation of the rectangle.
        """
        return f"Rectangle({self._width}, {self._height})"


# Test the Rectangle class
if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    # Test the string representation
    print(str(my_rectangle))   # Should print the rectangle as grid of '#' characters
    print(repr(my_rectangle))  # Should show the official string representation of the object

    print("--")

    # Modify the rectangle's attributes and test again
    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)  # Should print a new rectangle with updated dimensions
    print(repr(my_rectangle))  # Should show the updated official representation
