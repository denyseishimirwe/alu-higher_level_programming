#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Print each integer in the row with a space in between, no trailing space
        print(" ".join("{:d}".format(num) for num in row))
