#!/usr/bin/python3

def no_c(my_string) -> str:
    return "".join(char for char in my_string if char not in 'Cc')
