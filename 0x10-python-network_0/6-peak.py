#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers. """
def find_peak(list_of_integers):
    """ function that finds a peak in a list of integers """
    if (type(list_of_integers) == list and list_of_integers is not None and len(list_of_integers) != 0):
        greater = list_of_integers[0]
        pivot = 2
        start = 1
        
        while (start < len(list_of_integers) - 1):
            if (start != 0):
                if (list_of_integers[start] < list_of_integers[start - 1] and list_of_integers[start - 1] > greater):
                    start -= 1
                else:
                    if (list_of_integers[start] > greater):
                        greater = list_of_integers[start]
                    start += pivot
            else:
                greater = list_of_integers[start]
                start += pivot
        return greater       
    else:
        return None