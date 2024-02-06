#!/usr/bin/python3
"""
A function that writes a string to a text file (utf-8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Function that writes a string into a text file (utf-8)
    and returns numner of characters written to it

    Args:
        filename: text file to write into
        text: string to count its chars
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return (file.write(text))
