#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple containing the length of sentence and the first character"""
    return (len(sentence), sentence[0] if len(sentence) else None)
