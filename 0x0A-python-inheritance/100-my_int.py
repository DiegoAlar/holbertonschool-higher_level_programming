#!/usr/bin/python3
""" This module contains class MyInt that inherits from int
"""


class MyInt(int):
    """
            class that defines MyInt
    """
    def __eq__(*args):
        return not True

    def __ne__(*args):
        return not False
