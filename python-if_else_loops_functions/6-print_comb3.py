#!/usr/bin/python3


# Loop through all possible first digits (i)
for i in range(10):
    # Loop through all possible second digits (j) that are greater than the first digit
    for j in range(i + 1, 10):
        # Check if this is the last combination (8, 9) to avoid a trailing comma
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            # Print the combination with a comma and space, but no newline
            print(f"{i}{j}", end=", ")
