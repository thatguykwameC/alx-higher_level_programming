#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds multiples of 2"""
    return [True if num % 2 == 0 else False for num in my_list]
