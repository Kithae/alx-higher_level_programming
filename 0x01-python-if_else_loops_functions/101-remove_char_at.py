#!/usr/bin/python3
def remove_char_at(str, n):
    a = 0
    copy = ''
    for x in str:
        if a == n:
            a += 1
            continue
        copy += x
        a += 1
    return copy
