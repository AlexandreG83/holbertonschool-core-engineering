#!/usr/bin/env python3

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
