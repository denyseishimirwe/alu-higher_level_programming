#!/usr/bin/python3


def safe_print_integer(value):
    """
    Prints an integer using '{:d}'.format() and returns True if successful.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    # Test cases
    values = [89, -89, "School"]

    for value in values:
        has_been_print = safe_print_integer(value)
        if not has_been_print:
            print("{} is not an integer".format(value))
