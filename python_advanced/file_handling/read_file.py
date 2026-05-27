#!/usr/bin/env python3
"""Module that reads a text file and prints it to stdout."""


def read_file(filename=""):
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        print(f.read(), end="")
