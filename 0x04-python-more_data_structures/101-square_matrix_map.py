#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """Returns the square values of all integers in a matrix"""
    return list(map((lambda row: list(map((lambda x: x**2), row))), matrix))
