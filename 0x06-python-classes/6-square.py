#!/usr/bin/python3
class Square:
    """Class that defines instance given size"""
    def __init__(self, size=0, position=(0, 0)):
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
        if type(position) == tuple:
            if len(position) == 2:
                if type(position[0]) == int and type(position[1]) == int:
                    self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
    """" test """
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @size.setter
    def position(self, position):
        if type(position) == tuple:
            if len(position) == 2:
                if type(position[0]) == int and type(position[1]) == int:
                    self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for line in range(self.__position[1]):
                print()
            for side in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for side2 in range(self.__size):
                    print("#", end="")
                print()
