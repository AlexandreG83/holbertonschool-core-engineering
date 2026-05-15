#!/usr/bin/env python3
"""Defines a square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle. """

    def __init__(self, size):
        """ Initialize a Square instance. """
        super().__init__(size, size)

    def __str__(self):
        """ Return the string representation of the Square. """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
