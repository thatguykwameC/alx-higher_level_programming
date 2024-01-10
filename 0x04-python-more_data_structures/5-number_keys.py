#!/usr/bin/python3

def number_keys(a_dictionary: dict) -> int:
    """Returns the number of keys in a dictionary"""
    return len(a_dictionary.keys()) if isinstance(a_dictionary, dict) else None
