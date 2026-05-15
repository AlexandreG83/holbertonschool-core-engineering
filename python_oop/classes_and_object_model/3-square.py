#!/usr/bin/env python3
"""Square class with size and area method"""


class Square:
    """Defines a square"""

    def __init__(self, size):
    """Initialize the square with a size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
    """Calculate and return the area of the square"""

        return self.__size * self.__size
