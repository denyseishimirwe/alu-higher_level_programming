#!/usr/bin/python3


"""
Module for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF-8 file and returns the number of character added.
    Args:
        filename (str): The name of the file to append to.
        text (str): The text to be appended to the files.
    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)


# Test case
if __name__ == "__main__":
    text = "This School is cool!\n"
    nb_characters_added = append_write("file_append.txt", text)
    print(nb_characters_added)
