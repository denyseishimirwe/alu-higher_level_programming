#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of my_list that are integers.
    Returns the number of integers printed.
    """
    count = 0
    for i in range(x):  # Do not handle IndexError; let Python raise it
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count


if __name__ == "__main__":
    # Test cases
    my_list = [1, 2, 3, 4]

    nb_print = safe_print_list_integers(my_list, len(my_list) + 4)
    print("nb_print: {:d}".format(nb_print))
