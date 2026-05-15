#!/usr/bin/env python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """compute the area of the geometry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer
        Args:
            name (str): The name of the parameter
            value: The value to validate
        Raises:
            TypeError: If value is not an integer or is a boolean
            ValueError: If value is less than or equal to 0
        """

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
