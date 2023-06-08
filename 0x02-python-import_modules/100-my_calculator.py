#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = len(sys.argv) - 1
    if a != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    b = sys.argv[2]
    if b != '+' and b != '-' and b != '*' and b != '/':
        print("Invalid operators. Please use only these operators: +, -, * & /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    x = int(sys.argv[1])
    y = int(sys.argv[3])

    if y == '+':
        print("{} + {} = {}".format(x, y, add(x, y)))
    elif y == '-':
        print("{} - {} = {}".format(x, y, sub(x, y)))
    elif y == '*':
        print("{} * {} = {}".format(x, y, mul(x, y)))
    else:
        print("{} / {} = {}".format(x, y, div(x, y)))
