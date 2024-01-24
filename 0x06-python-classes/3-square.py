#!/usr/bin/python3
"""Defines a blueprint for class square"""


class Square:
    """
    Represents the class square with a private instance
    """

    def __init__(self, size: int = 0):
        """
        Initializes the class square

        Args:
            size (int, optional): the size of the square. (Default = 0)
        """
        # size must be an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # it should be greater than or equal to zero
        if size < 0:
            raise ValueError("size must be >= 0")

        # set the size of the Square if all goes well
        self.__size = size

    def area(self) -> int:
        """
        Calculates and returns area of the square
        """
        return self.__size**2
