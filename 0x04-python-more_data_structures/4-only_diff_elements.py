#!/usr/bin/python3

def only_diff_elements(set_1: set, set_2: set) -> set:
    """Returns a set of all elements present in one set"""
    return set(set_1.symmetric_difference(set_2))
