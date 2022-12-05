#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Returns a list of booleans depnding on if element is a multiple of 2"""
    return [not bool(x % 2) for x in my_list]
