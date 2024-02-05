#!/usr/bin/python3
"""A module that inherits from the Rectangle class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Models a square shape object."""

    def __init__(self, size: int):
        """
        Initializes a Square object.

        Args:
            size: The size of the square.
        """
        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size**2
