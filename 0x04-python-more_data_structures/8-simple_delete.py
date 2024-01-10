#!/usr/bin/python3

def simple_delete(a_dictionary: dict, key: str = "") -> dict:
    """Deletes a key in a dictionary if present else return same dictionary"""
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
