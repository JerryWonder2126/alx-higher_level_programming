#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key/value pair if key exists in dictionary"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
