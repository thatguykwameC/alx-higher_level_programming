#!/usr/bin/python3
"""
A module that returns True if the object is exactly an
instance of the specified class.
"""


def is_same_class(obj: object, a_class):
    """
    Returns True if `obj` is an instance of `a_class`.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check if obj  is an instance
    """
    return type(obj) is a_class
