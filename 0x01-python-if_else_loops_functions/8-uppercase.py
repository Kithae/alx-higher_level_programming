#!/usr/bin/python3
def str_uper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(str):
    new = ""
    for char in str:
        new += "%c" % str_uper(char)
    print("{:s}".format(new))
