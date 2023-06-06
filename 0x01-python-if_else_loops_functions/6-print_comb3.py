#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if a == 8 and b == 9:
            print("{}{}".format((a), (b)))
            break
        if a < b:
            print("{}{}".format((a), (b)), end=', ')
