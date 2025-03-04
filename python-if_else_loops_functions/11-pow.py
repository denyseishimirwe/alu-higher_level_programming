#!/usr/bin/python3


def pow(a, b):
    # Case 1: If b is 0, return 1 (since any number to the power of 0 is 1)
    if b == 0:
        return 1
    # Case 2: If b is positive, multiply a by itself b times
    elif b > 0:
        result = 1
        for _ in range(b):
            result *= a
        return result
    # Case 3: If b is negative, return 1 / (a^|b|)
    else:
        result = 1
        for _ in range(abs(b)):
            result *= a
        return 1 / result
