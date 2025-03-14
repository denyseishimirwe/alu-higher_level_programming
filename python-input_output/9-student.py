#!/usr/bin/python3


"""
Student class with public instance attributes and a method to retrieve
a dictionary representation of the instance.
"""


class Student:
    """Define a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of the Student instance."""
        return self.__dict__
