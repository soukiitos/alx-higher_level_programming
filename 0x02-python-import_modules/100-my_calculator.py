#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] in list(ops.keys()):
        i = int(sys.argv[1])
        j = int(sys.argv[3])
        op = ops[sys.argv[2]]
        result = op(i, j)
        print("{:d} {:s} {:d} = {:d}".format(i, sys.argv[2], j, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
