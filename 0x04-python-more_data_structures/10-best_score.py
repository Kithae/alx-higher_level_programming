#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    tempscore = 0
    a = None
    for key, value in a_dictionary.items():
        if value > tempscore:
            tempscore = value
            a = key
    return a
