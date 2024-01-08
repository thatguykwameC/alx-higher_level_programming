#!/usr/bin/python3

def max_integer(my_list=[]):
    """Returns the largest number in a list of integers"""
    return None if not my_list else sorted(my_list)[-1]
