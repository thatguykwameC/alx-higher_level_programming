#!/usr/bin/python3
def magic_string():
    magic_string.counter = getarr(magic_string, 'counter', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.counter - 1)
