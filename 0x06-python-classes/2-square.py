#!/usr/bin/python3
"""Defines a blueprint for class square"""


class Square:
    """Represents the class square with a private instance"""

    def __init__(self, size=0):
        """
        Initalizes the class square
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
