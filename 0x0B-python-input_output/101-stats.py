#!/usr/bin/python3
'''Define Log parsing'''
import sys


size = 0
code = {'200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0}
t = 0


'''Read stdin line by line and computes metrics'''


def print_stats():
    '''Print the stats'''
    print("File size: ", size)
    for i, j in sorted(code.items()):
        if j != 0:
            print(f"{i}: {j}")


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
            print_stats()
    print_stats()

except KeyboardInterrupt:
    print_stats()
