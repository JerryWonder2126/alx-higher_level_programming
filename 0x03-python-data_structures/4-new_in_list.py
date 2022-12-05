#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """"Replace an element in a copied list at a specific position."""
    list_copy = my_list.copy()
    if not (idx >= len(list_copy) or idx < 0):
        list_copy[idx] = element
    return list_copy
