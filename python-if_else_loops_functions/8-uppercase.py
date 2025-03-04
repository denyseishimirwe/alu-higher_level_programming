#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':  # Check if it's a lowercase letter
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Keep the character unchanged
    print("{}".format(result))
