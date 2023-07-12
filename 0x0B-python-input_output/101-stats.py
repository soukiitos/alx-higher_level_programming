#!/usr/bin/python3
'''Define Log parsing'''


def print_stats(size, code):
    '''Print the stats and Read stdin line by line and computes metrics'''
    print("File size: ", size)
    for i, j in sorted(code.items()):
        if j != 0:
            print(f"{i}: {j}")


if __name__ == "__main__":
    import sys

    size = 0
    code = {'200': 0, '301': 0, '400': 0, '401': 0,
            '403': 0, '404': 0, '405': 0, '500': 0}
    t = 0

    try:
        for line in sys.stdin:
            line = line.split()
            if len(line) >= 2:
                if line[-2] in code:
                    code[line[-2]] += 1
                    t += 1
                    try:
                        size += int(line[-1])
                    except ValueError:
                        pass
            if t % 10 == 0:
                print_stats(size, code)
        print_stats(size, code)
    except KeyboardInterrupt:
        print_stats(size, code)
