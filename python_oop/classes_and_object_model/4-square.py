#!/usr/bin/env python3

"""
spam@camelot:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
"""


class Square:
    """Represents a square object.

    Attributes:
        __size (int): Size of the square side.
    """

    def __init__(self, size=0):
        """Initialize a Square instance."""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square side.
        Args:
            value (int): Length of the square side (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Compute the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2
