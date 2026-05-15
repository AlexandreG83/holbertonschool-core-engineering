#!/usr/bin/env python3
"""Square module.

This module defines a Square class that represents a square and provides
a method to compute its area.
"""


class Square:
    """Represents a square object.

    Attributes:
        __size (int): Size of the square side.
    """

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): Length of the square side (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2
