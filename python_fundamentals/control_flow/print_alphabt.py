for i in range(26):
    if i == 4 or i == 16:  # 4 is the index for 'e' and 16 is the index for 'q'
        continue  # Skip 'e' and 'q'
    letter = chr(97 + i)  # 97 is the ASCII code for 'a'
    print(letter, end='')