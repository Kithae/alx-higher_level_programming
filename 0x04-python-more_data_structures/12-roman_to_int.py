#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    r_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
            }
    new_num = 0
    last_num = 0
    for c in reversed(roman_string):
        if a not in r_dict:
            return 0
        value = r_dict[a]
        if value >= last_num:
            new_num += value
        else:
            new_num -= value
        last_num = value
    return new_num
