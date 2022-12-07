#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key with the highes value"""
    if not a_dictionary:
        return None
    highest_score = 0
    highest_key = None
    for x, y in a_dictionary.items():
        if y > highest_score:
            highest_score = y
            highest_key = x
    return highest_key
