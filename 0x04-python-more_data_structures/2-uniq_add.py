#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_a = set(my_list)
    result = 0
    for s in set_a:
        result += s
    return result
