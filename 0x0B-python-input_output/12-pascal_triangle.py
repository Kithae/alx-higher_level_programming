#!/usr/bin/python3
"""module for a Pascal's Triangle."""


def pascal_triangle(n):
    """Pascal's Triangle representation.

    Returns triangle integers list.
    """
    if n <= 0:
        return []

    ntri = [[1]]
    while len(ntri) != n:
        mytri = ntri[-1]
        tmp = [1]
        for a in range(len(mytri) - 1):
            tmp.append(mytri[a] + mytri[a + 1])
        tmp.append(1)
        ntri.append(tmp)
    return ntri
