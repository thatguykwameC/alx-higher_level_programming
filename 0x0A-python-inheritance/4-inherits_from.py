#!/usr/bin/python3
"""
A module that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class, else False
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check if `obj` is an instance of.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
