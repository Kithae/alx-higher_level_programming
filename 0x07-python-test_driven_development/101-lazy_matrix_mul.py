#!/usr/bin/python3
"""Module lazy_matrix_mul
Uses NumPy to multiply a Matrix.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ uses matmul to return the product of m_a and m_b
    """
    return numpy.matmul(m_a, m_b)
