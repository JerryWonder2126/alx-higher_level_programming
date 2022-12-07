#!/usr/bin/python3
def roman_to_int(roman_string):
    """A function that converts a Roman numeral to an integer."""

    if not roman_string or type(roman_string) != str:
        return 0

    standard = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    extended = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    string_len = len(roman_string)
    end = string_len
    number = 0

    while end >= 1:
        if end >= 2:
            two_character = roman_string[end - 2: end]
            if two_character in extended:
                number += extended[two_character]
                end -= 2
                print("{} - {}".format(two_character, extended[two_character]))
                continue
        character = roman_string[end - 1]
        number += standard[character]
        end -= 1

    return number
