#!/usr/bin/python3

def roman_to_int(roman_string: str) -> int:
    """Converts roman numerals to integers"""
    rom_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    return sum(
        rom_numerals.get(roman_string[i], 0)
        if i == 0
        or rom_numerals.get(roman_string[i], 0)
        <= rom_numerals[roman_string[i - 1]]

        else rom_numerals.get(roman_string[i], 0)
        - 2 * rom_numerals.get(roman_string[i - 1], 0)
        for i in range(len(roman_string))
    )
