#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_roman = 0
    for a in range(len(roman_string)):
        if a > 0 and r_dict[roman_string[a]] > r_dict[roman_string[a - 1]]:
            new_roman += r_dict[roman_string[a]] - 2 * \
                        r_dict[roman_string[a - 1]]
        else:
            new_roman += r_dict[roman_string[a]]
    return new_roman
