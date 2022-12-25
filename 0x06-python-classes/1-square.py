#!/usr/bin/python3
"""This module defines a class of Square"""


class Square:
    """An class called square

    Attributes:
    attr1 (size): size of the square
    """
    __size = None

    def __init__(self, size):
        """
        Args:
        size: size for __size attribute of the class instance
        """
        self.__size = size
