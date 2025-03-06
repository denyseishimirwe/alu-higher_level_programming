#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

# Test cases for the print_matrix_integer function
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix1)  # Expected output: 1 2 3 \n 4 5 6 \n 7 8 9

print("--")

matrix2 = [
    [1, 2],
    [3, 4]
]
print_matrix_integer(matrix2)  # Expected output: 1 2 \n 3 4

print("--")

# Test with an empty matrix
matrix3 = []
print_matrix_integer(matrix3)  # Expected output: nothing (no output)
