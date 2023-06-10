#!/usr/bin/python3
def max_integer(my_list=[]):
    """a function for finding biggest list int."""
    if len(my_list) == 0:
        return (None)
    largest = my_list[0]
    for a in range(len(my_list)):
        if my_list[a] > big:
            largest = my_list[a]
    return (largest)
