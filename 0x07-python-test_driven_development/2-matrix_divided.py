#!/usr/bin/python3
""" this module contains only one function """


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix """
    new_list = []
    new_m = []
    err_mge = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
            raise TypeError(err_mge)
    elif type(matrix[0]) is not list or len(matrix[0]) is 0:
            raise TypeError(err_mge)
    lon = len(matrix[0])
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_mge)
        elif len(row) != lon:
            raise TypeError("Each row of the matrix must have the same size")
        elif type(row) != list:
            raise TypeError(err_mge)
        else:
            for item in row:
                if type(item) is not int and type(item) is not float:
                    raise TypeError(err_mge)
                else:
                    new_list.append(round((item / div), 2))
            new_m.append(new_list)
            new_list = []
    return new_m
