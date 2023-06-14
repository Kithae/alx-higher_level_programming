#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_new = {key: a_dictionary[key] for key in sorted(a_dictionary.keys())}
    for key, value in dict_new.items():
        print(f"{key}: {value}")
