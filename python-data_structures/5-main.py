#!/usr/bin/python3
no_c = __import__('5-no_c').no_c

# Test cases for the no_c function
print(no_c("Best School"))  # Expected output: "Best Shool"
print(no_c("Holac"))        # Expected output: "Hola"
print(no_c("CCCCC"))        # Expected output: ""
print(no_c("abcABC"))       # Expected output: "ab"
print(no_c(""))             # Expected output: ""
