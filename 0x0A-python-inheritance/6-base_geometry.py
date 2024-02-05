#!/usr/bin/python3
"""A module that defines a class BaseGeometry"""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Returns the area of a shape"""
        raise Exception("area() is not implemented")
