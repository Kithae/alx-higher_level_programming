#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for a in my_string:
        if a != 'c' and a != 'C':
            new_str += a
    return (new_str)
