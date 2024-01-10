#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of integers in tuples"""
    if my_list and len(my_list):
        numerator = 0
        denominator = 0
        for t in my_list:
            numerator += (t[0] * t[1])
            denominator += (t[1])
        return (numerator/denominator)
    return 0
