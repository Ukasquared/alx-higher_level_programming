#!/usr/bin/python3

"""
This module divides all element of a matrix
"""

def matrix_divided(matrix, div):
    """ This module divides integers or floats
    Args:
        matrix: list of list of integers and float
        div: dividend
    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    if div is None:
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    oldlen = len(matrix[0])
    matrix_val = []
    for i in range(len(matrix)):
        matrix_val.append([])
        if not oldlen == len(matrix[i]):
            raise TypeError("matrix must have each row with the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (float, int)):
               raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
            matrix_val[i].append(round(matrix[i][j] / div, 2))
    return (matrix_val)
