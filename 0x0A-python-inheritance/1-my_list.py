#!/usr/bin/python3
""" This module contains function print_sorted
"""


class MyList(list):
    """
        Class that inherits from list class
    """

    def print_sorted(self):
        """ This function
            Args:
                self: references to the object
        """

        print(sorted(self))
