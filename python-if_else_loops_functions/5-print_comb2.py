#!/usr/bin/python3
for i in range(100):
    # Print the number with two digits, adding a comma and space after each except the last one
    print(f"{i:02}", end=", " if i < 99 else "\n")
