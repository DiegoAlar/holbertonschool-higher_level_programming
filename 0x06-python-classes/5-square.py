#!/usr/bin/python3
class Square:
    """Class that defines instance given size"""
    def __init__(self, size=0):
        """init method to initialized variables
        Args:
            size (int): the size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """" test """
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for side in range(self.__size):
                for side2 in range(self.__size):
                    print("#", end="")
                print()
