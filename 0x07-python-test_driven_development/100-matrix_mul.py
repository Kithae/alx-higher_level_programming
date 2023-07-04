#!/usr/bin/python3
"""Module matrix_mul
Returns the product of two matrices.
"""


def matrix_mul(m_a, m_b):
    """Returns the product matrix of m_a and m_b."""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for j in m_a:
        if type(j) is not list:
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for nrows in m_a:
        for j in nrows:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for nrows in m_b:
        for j in nrows:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    len_row = []
    for nrows in m_a:
        len_row.append(len(nrows))
    if not all(elem == len_row[0] for elem in len_row):
        raise TypeError("each row of m_a must should be of the same size")
    len_row = []
    for nrows in m_b:
        len_row.append(len(nrows))
    if not all(elem == len_row[0] for elem in len_row):
        raise TypeError("each row of m_b must should be of the same size")

    col_a = 0
    for ncols in m_a[0]:
        col_a += 1
    row_b = 0
    for nrows in m_b:
        row_b += 1

    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for c in range(len(m_b[0]))] for d in range(len(m_a))]

    for s in range(len(m_a)):
        for t in range(len(m_b[0])):
            for v in range(len(m_b)):
                result[s][t] += m_a[s][v] * m_b[v][t]

    return result
