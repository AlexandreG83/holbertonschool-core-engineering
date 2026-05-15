#!/usr/bin/env python3

class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """compute the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
