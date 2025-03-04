#!/usr/bin/python3

# Loop through all possible first digits (i)
for i in range(10):
    # Loop through all possible second digits (j) that are greater than the first digit
    for j in range(i + 1, 10):
        # Print the combination with a comma and space except for the last combination (8, 9)
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")
