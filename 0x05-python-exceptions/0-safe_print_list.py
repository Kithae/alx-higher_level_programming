#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    tally = 0
    for a in range(x):
        try:
            print(f"{my_list[a]}", end="")
            tally += 1
        except IndexError:
            break
    print()
    return(tally)
