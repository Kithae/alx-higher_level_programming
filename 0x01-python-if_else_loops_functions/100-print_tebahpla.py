#!/usr/bin/python3
a = 122
while a > 64:
    char = chr(a)
    print("{}".format(char), end='')
    if a % 2 == 0:
        a -= 33
    else:
        a += 31
    if a == 96:
        break
