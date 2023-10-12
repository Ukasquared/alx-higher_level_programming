#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []

    def square(x):
        return (x ** 2)
    for index in matrix:
        each_matrix = list(map(square, index))
        new_matrix.append(each_matrix)
    return new_matrix
