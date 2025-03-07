#!/usr/bin/python3
"""Returns list of attributes and methods of an object."""

def lookup(obj):
    """
    Returns a list of attributes and methods of the object.
    """
    return dir(obj)

# Example cases
class MyClass1:
    """ A simple class """
    pass

class MyClass2:
    my_attr1 = 89
    def one_meth(self):
        pass

if __name__ == "__main__":
    # Test cases
    print(lookup(int))           # Expected: List of attributes and methods of int
    print(lookup(float))         # Expected: List of attributes and methods of float
    print(lookup(object))        # Expected: List of attributes and methods of object
    print(lookup(list))          # Expected: List of attributes and methods of list
    print(lookup(MyClass1))      # Expected: List of inherited attributes and methods of MyClass1
    print(lookup(MyClass2))      # Expected: List of attributes and methods of MyClass2
    print(lookup(MyClass))       # Custom case: ['my_class', 'is', 'empty']
