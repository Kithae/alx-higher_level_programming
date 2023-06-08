#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for x in sys.argv:
        if x != sys.argv[0]:
            result += int(x)
    print(result)
