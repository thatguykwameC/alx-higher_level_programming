#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """This function returns a matrix with it's elements squared"""
    return[list(map(lambda element: element**2, row)) for row in matrix]
