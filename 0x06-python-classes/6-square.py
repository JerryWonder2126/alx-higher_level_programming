#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """A class named Square
    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0, position=(0,0)):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for __size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for __size

        Args:
        size (int): the value to be assigned to __size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the instance
        Returns:
        int: the area of the square
        """
        return self.__size**2

    def my_print(self):
        """Prints in stdout the square with the # character"""
        if self.__size > 0:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
