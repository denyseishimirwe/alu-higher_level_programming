#!/usr/bin/python3


"""
Function that returns a list of lists of integers representing
Pascal's Triangle.

The function generates Pascal's Triangle for a given number of rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n rows.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists, each containing the elements of each
              row of the triangle. An empty list is returned if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
