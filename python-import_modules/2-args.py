#!/usr/bin/python3
import sys


def main():
    # Get the number of arguments
    arg_count = len(sys.argv) - 1  # Exclude the script name itself
    
    # Print the number of arguments
    if arg_count == 0:
        print(f"0 arguments.")
    elif arg_count == 1:
        print(f"1 argument:")
    else:
        print(f"{arg_count} arguments:")
    
    # Print each argument with its position
    for i in range(1, arg_count + 1):
        print(f"{i}: {sys.argv[i]}")


# Ensure this code runs only when executed as a script
if __name__ == "__main__":
    main()
