#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements, filling with 0 if needed
    a1, a2 = tuple_a + (0, 0)
    b1, b2 = tuple_b + (0, 0)
    
    # Return a tuple with the sums of the corresponding elements
    return (a1 + b1, a2 + b2)
