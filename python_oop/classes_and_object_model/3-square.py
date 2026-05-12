#!/usr/bin/env python3

"""
spam@camelot:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
"""


class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2
