#!/usr/bin/python3

"""This module defines a locked class"""


class LockedClass:
    """
    Prevents the dynamic creation of new instance attributes, allowing only
    the attribute `first_name`.
    """

    __slots__ = ["first_name"]
