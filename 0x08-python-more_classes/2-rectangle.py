#!/usr/bin/python3

"""This module defines a class Rectangle"""


class Rectangle:
    """Represents a geometric rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrives the width of the rectangle

        Returns: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args: The value for the width
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
        Retrives the height of the rectangle

        Returns: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args: The value for the height
        """
        if not isinstance(value, int):
            raise TypeError("height  must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns: The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns: The perimeter of the recctangle
        """
        return (
            2 * (self.width + self.height) if self.width and self.height else 0
        )
