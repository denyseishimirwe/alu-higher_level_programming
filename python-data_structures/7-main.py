#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

# Test cases for the add_tuple function
tuple1 = (1, 2)
tuple2 = (3, 4)
new_tuple = add_tuple(tuple1, tuple2)
print(new_tuple)  # Expected output: (4, 6)

tuple3 = (1,)
tuple4 = (5, 6)
print(add_tuple(tuple3, tuple4))  # Expected output: (6, 8)

tuple5 = ()
tuple6 = (8, 9)
print(add_tuple(tuple5, tuple6))  # Expected output: (8, 9)
