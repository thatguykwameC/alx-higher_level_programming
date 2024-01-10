#!/usr/bin/python3

def common_elements(set_1: set, set_2:set) -> set:
    """Returns a set of common elements"""
    return set(set_1.intersection(set_2))
