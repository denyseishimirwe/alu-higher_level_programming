#!/usr/bin/python3


"""
Student class with a method to retrieve a filtered dictionary representation
based on given attributes.
"""


class Student:
    """Define a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance,
        filtered by the given attributes (if provided).
        """
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
