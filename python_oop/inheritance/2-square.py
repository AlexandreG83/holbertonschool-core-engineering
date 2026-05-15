#!/usr/bin/env python3
"""Defines a square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle. """

    def __init__(self, size):
        """ Initialize the square with size. """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Return the string representation of the square. """
        return "[Square] {}/{}".format(self.__size, self.__size)
