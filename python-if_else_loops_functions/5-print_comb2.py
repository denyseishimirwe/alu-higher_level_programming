#!/usr/bin/python3
for i in range(0, 99):  # Loop from 0 to 98
    print("{:02d}".format(i), end=", " if i < 98 else "\n")  # Print numbers with two digits
