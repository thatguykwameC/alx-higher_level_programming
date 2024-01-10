#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces occurences of elements by another in a list"""
    return list(
        map(lambda element: replace if element == search else element, my_list)
    )
