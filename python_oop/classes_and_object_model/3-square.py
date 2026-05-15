#!/usr/bin/env python3
"""Square class with size and area method"""


class Square:
    """Defines a square"""

    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size * self.__size
