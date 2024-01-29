#!/usr/bin/python3

"""This module defines a class Rectangle"""


class Rectangle:
    """Represents a geometric rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with specified width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the Rectangle

        Returns: The width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets and updates the width of the Rectangle

        Args: Value - The value for the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the Rectangle

        Returns: The height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets and updates the height of the Rectangle

        Args: Value - The value for the height
        """
        if not isinstance(value, int):
            raise TypeError("height  must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
