#!/usr/bin/python3
""" This module contains class Rectangle
"""


class Rectangle:
    """
            Class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Init method to initialized private variables
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.width is 0 or self.height is 0:
            return ""
        return ((str(self.print_symbol) * self.width + '\n') *
                (self.height - 1) + str(self.print_symbol) * self.width)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """
        Public instance method that returns the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance function that returns the rectangles's perimeter
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * self.__width + self.__height * 2
