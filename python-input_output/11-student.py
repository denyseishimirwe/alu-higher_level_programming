#!/usr/bin/python3


"""
Student class that defines a student, with methods to serialize and
deserialize the instance to and from JSON format.
"""


class Student:
    """
    A class that represents a student.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is provided (a list of strings), only the attributes
        in this list will be included in the dictionary. Otherwise,
        all attributes will be included.

        Args:
            attrs (list, optional): A list of attribute names to include
                                     in the dictionary.

        Returns:
            dict: A dictionary representation of the student instance.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values
        from a JSON dictionary.

        Args:
            json (dict): A dictionary with key-value pairs to update
                         the student attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
