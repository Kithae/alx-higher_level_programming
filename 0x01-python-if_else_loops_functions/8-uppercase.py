#!/usr/bin/python3
def upper(x):
    for y in x:
        charac = ord(y)
        if charac > 96 and charac < 123:
            charac -= 32
        print("{}".format(chr(charac)), end='')
    print('')
