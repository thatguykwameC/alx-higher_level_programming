#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
     """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to check attributes and methods for.
    """
    return dir(obj)
