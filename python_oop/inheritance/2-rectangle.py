#!/usr/bin/env python3

import base_geometry
BaseGeometry = base_geometry.BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
