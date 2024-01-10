#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """Multiplies values of a list using map"""
    return list(map(lambda x: x * number, my_list))
