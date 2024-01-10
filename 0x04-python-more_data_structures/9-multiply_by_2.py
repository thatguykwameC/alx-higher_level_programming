#!/usr/bin/python3

def multiply_by_2(a_dictionary: dict) -> dict:
    """Returns a new dictionary with all it's values doubled"""
    return {
        key: value * 2
        for key, value in a_dictionary.items()
        if isinstance(value, int)
    }
