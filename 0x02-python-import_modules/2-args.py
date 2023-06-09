#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1

    if length == 0:
        print("{} arguments.".format(length))
    elif length > 1:
        print("{} arguments:".format(length))
    else:
        print("{} arguments:".format(length))
        print("{}: {}".format(length, sys.argv[1]))
    for i in range(length):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
