#!/usr/bin/python3
for a in range(100):
    if a == 99:
        print("{}".format(a))
        break
    print("{:02}".format(a), end=", ")
