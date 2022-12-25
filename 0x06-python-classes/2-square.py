#!/usr/bin/python3
"""This module defines a class of Square"""


class Square:
    """An class called square

    Attributes:
    attr1 (size): size of the square
    """

    def __init__(self, size=0):
        """
        Args:
        size: size for __size attribute of the class instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
