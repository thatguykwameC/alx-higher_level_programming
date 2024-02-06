#!/usr/bin/python3
"""
A function that reads a text file (utf-8) and prints to stdout
"""


def read_file(filename=""):
    """
    Function that reads a text (utf-8) file

    Args:
        filename: name of file(.txt) to read

    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
