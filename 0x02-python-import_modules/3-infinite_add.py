#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = 0
    for j in range(len(sys.argv) - 1):
        i += int(sys.argv[j + 1])
    print("{}".format(i))
