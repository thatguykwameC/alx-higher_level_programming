#!/usr/bin/python3
"""
A function that appends a string to the end of a text file
(utf-8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    A function that appends a string to the end of a text file
    (utf-8) and returns the number of characters added

    Args:
        filename: text file to write/append into
        text: string to append to file
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        return (file.write(text))
