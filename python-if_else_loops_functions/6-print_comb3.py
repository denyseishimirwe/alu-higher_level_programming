#!/usr/bin/python3
for i in range(0, 9):  # First digit ranges from 0 to 8
    for j in range(i + 1, 10):  # Second digit ranges from i+1 to 9 (ensures no duplicates)
        print("{:02d}".format(i) + "{:02d}".format(j), end=", " if (i < 8 or j < 9) else "\n")
