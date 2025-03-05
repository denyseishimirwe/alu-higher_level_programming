#!/usr/bin/python3
import sys


# Main function to handle the logic
def main():
    # Get the arguments from the command line (excluding the script name)
    arguments = sys.argv[1:]

    # If there are arguments, sum them up
    if arguments:
        total = sum(int(arg) for arg in arguments)  # Sum of all arguments after converting them to integers
    else:
        total = 0  # If no arguments, the sum is 0

    print(total)

# Ensure this code runs only when executed as a script
if __name__ == "__main__":
    main()
