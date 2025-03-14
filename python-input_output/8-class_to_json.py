#!/usr/bin/python3


"""
Function that returns the dictionary description with simple data structure
(list, dict, string, int, and bool) for JSON serialization of an object.
"""


class MyClass:
    """ My class with public and private attributes
    """

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.__private_attribute = "private"
        self.my_dict = {"key": "value"}
        self.my_list = [1, 2, 3]

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)


def class_to_json(obj):
    """Return the dictionary description for JSON serialization"""
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (str, int, bool, list, dict))}
