#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns matrix with all its value squared"""
    return [[x**2 for x in row] for row in matrix]
