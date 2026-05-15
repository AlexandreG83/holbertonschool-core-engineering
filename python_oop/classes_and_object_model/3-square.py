#!/usr/bin/env python3
"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size):
        """Initialize size"""
        self.__size = size

    def area(self):
        """Return area of square"""
        return self.__size ** 2
