#!/usr/bin/python3
"""
Module matrix_divided
Division by a number of each matrix element
"""


def matrix_divided(matrix, div):
    """Returns the division results as a list of list
    the new matrix is rounded to 2 decimals.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for nrows in matrix:
        if len(nrows) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for a in nrows:
            if type(a) is not int and type(a) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_row = []
    for nrows in matrix:
        len_row.append(len(nrows))
    if not all(elem == len_row[0] for elem in len_row):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(a / div, 2) for a in nrows] for nrows in matrix]

    return new_matrix
