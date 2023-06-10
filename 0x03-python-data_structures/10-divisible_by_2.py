#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """a function for finding multiples of 2."""
    mul = []
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)
    return (mul)
