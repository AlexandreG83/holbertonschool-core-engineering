#!/usr/bin/env python3
"""Defines a square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle. """

    def __init__(self, size):
        """ Initialize a Square instance. """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = sizes
