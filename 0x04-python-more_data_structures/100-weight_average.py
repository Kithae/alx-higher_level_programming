#!/usr/bin/python3
def weight_average(my_list=[]):
    nscore = 0
    nnum = 0
    if not my_list:
        return nscore
    for t in my_list:
        nscore += (t[0] * t[1])
        nnum += t[1]
    nscore /= nnum
    return nscore
