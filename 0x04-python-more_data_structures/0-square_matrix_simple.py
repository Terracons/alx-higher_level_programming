#!/usr/bin/python3
def mult_2(mylist):
    new = []
    for i in mylist:
        new.append(i**2)
    return new


def square_matrix_simple(matrix=[]):
    temp_matrix = matrix.copy()
    temp_matrix = list(map((lambda x: mult_2(x)), temp_matrix))
    return temp_matrix
