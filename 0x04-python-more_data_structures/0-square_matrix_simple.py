#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for r in matrix:
        curr_row = list(map(lambda x: x ** 2, r))
        new_matrix.append(curr_row)
    return new_matrix
