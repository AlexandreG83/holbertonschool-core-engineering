#!/usr/bin/env python3
def print_last_digit(number):
    last_digit = abs(number)
    print(last_digit % 10, end="")
    return last_digit % 10
