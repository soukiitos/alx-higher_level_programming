#!/usr/bin/python3
def add_args(argv):
    i = len(argv) - 1
    if i != 0:
        j = 1
        add = 0
        while j <= i:
            add += int(argv[j])
            j += 1
            print("{:d}".format(add))
    else:
        print("{:d}".format(i))
        return


if __name__ == "__main__":
    import sys
    add_args(sys.argv)
