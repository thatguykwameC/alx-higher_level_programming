#!/usr/bin/python3

"""This module defines a class Rectangle"""


class Rectangle:
    """Represents a geometric rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrives the width of the rectangle

        Returns: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value=0):
        """
        Sets the width of the rectangle

        Args: The value of the width
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
    def height(self, value=0):
        """
        Sets the height of the rectangle

        Args: The value for the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns: The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns: The perimeter of the rectangle
        """
        return (
            2 * (self.width + self.height) if self.width and self.height else 0
        )

    def __str__(self):
        """
        Returns a string representation of the rectangle with '#' characters.
        """
        str_rep = ""
        symbol = self.print_symbol

        if self.__width == 0 or self.__height == 0:
            return str_rep

        for i in range(self.__height):
            str_rep += str(symbol) * self.__width
            if (i != self.__height - 1):
                str_rep += '\n'

        return str_rep

    def __repr__(self):
        """
        Generates a string representation of the rectangle, using eval()

        Returns: The string representation of the rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Prints a message after the rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
