#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts roman numerals to integers"""
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0

    numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for num in roman_string:
        arabic = numerals[num]
        total += arabic if total < arabic * 5 else -arabic

        return total
