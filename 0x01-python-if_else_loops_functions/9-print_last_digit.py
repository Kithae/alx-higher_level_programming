#!/usr/bin/python3
def print_last_digit(x):
    digit_last = abs(x) % 10
    print(f"{digit_last}", end='')
    return digit_last
