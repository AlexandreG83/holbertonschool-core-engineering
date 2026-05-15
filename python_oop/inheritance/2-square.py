#!/usr/bin/env python3

Rectangle = __import__('1-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle. """

    def __init__(self, size):
        """ Initialize a Square instance. """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Return the string representation of the Square. """
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
