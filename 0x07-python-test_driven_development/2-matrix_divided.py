#!/usr/bin/python3
"""This program is about a function that divide
a matrix with a parameter
div( float or int), but cannot be divided by
zero
"""


def matrix_divided(matrix, div):
    """matrix_divided
    Divide all element of matrix by
    param 'div'
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    t_error1 = "matrix must be a matrix (list of lists) of integers/floats"
    t_error2 = "Each row of the matrix must have the same size"
    result_mat = []

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(t_error2)
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(t_error1)
            else:
                inner_list.append(round(items / div, 2))
        result_mat.append(inner_list)

    return result_mat
