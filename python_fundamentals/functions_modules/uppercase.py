#!/usr/bin/env python3

def uppercase(str):
    """Convert a string to uppercase.

    Args:
        text: The string to convert.

    Returns:
        The uppercase version of the string.
    """
    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
