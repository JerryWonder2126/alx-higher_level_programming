#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a dictionary with all its values mulitplied by 2"""
    return {x: y * 2 for x, y in a_dictionary.items()}
