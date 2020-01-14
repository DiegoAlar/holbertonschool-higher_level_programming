#!/usr/bin/python3
""" This module contains the function matrix_mul
"""
def matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices
    """
    new_m = []
    new_mm = []
    result = 0
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    rows_a = len(m_a)
    cols_b = len(m_b[0])
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row_a, row_b in m_a, m_b:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
        elif type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")
        elif len(m_a) is 0 or len(row_a) is 0:
            raise ValueError("m_a can't be empty")
        elif len(m_b) is 0 or len(row_b) is 0:
            raise ValueError("m_b can't be empty")
        for item_a, item_b in row_a, row_b:
            if type(item_a) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
            elif type(item_b) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
            elif len(row_a) is not cols_a:
                raise TypeError("each row of m_a must be of the same size")
            elif len(row_b) is not cols_b:
                raise TypeError("each row of m_b must be of the same size")
    for i in range(len(m_a)):
        if len(m_a[i]) is not rows_b:
            raise ValueError("m_a and m_b can't be multiplied")
        else:
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result += m_a[i][k] * m_b[k][j]
                new_m.append(result)
                result = 0
            new_mm.append(new_m)
            new_m = []
    return new_mm
