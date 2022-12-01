#!/usr/bin/python3

if __name__ == '__main__':
    """Adds up all numbers passed as arguments to the script"""
    import sys

    sum = 0

    for x in sys.argv[1:len(sys.argv)]:
        sum += int(x)

    print("{}".format(sum))
