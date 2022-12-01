#!/usr/bin/python3
if __name__ == '__main__':
    """Prints all arguments pass to the program"""
    import sys

    arg_length = len(sys.argv) - 1
    if arg_length:
        print("{} arguments{}".format(arg_length, ':'))
    else:
        print("{} arguments{}".format(arg_length, '.'))
    for x in range(1, arg_length + 1):
        print("{}: {}".format(x, sys.argv[x]))
