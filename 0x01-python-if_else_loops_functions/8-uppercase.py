#!/usr/bin/python3
def uppercase(str):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            upper_ascii = ord(char) - 32
            print("{:c}".format(upper_ascii), end='')
        else:
            print(char, end='')
