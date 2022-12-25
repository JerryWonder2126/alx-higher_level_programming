#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """A class named Square
    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        self.__size = size

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
        """Prints # a number of times, depending on the value of size"""
        if self.size > 0:
            for i in range(self.size):
                for j in range(self.size):
                    print('#', end='')
                print()
        else:
            print()
