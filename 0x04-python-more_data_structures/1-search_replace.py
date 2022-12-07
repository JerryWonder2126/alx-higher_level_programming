#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace search with replace in my_list"""
    def f(x):
        return x if x != search else replace
    return list(map(f, my_list))
