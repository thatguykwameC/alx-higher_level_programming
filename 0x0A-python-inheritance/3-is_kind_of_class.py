#!/usr/bin/python3
"""
A module that returns True if the object is an
instance of a class or inherited class
"""


def is_kind_of_class(obj: object, a_class):
    """
    Returns True if `obj` is an instance of `a_class`.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check if `obj` is an instance of.
    """
    return isinstance(obj, a_class)
