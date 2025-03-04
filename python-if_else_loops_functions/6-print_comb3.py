#!/usr/bin/python3

# Loop through all possible first digits (i)
for i in range(10):
    # Loop through all possible second digits (j) that are greater than the first digit
    for j in range(i + 1, 10):
        # If it's the last combination (89), print it without a comma
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            # For other combinations, print with a comma and space
            print(f"{i}{j}", end=", ")
