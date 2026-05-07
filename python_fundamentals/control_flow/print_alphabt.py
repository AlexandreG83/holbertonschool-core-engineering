#!/usr/bin/env python3
for i in range(26):
    if i == 4 or i == 16:
        continue
    letter = chr(97 + i)
    print(letter, end='')
