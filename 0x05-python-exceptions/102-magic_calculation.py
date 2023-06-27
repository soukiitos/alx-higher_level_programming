#!/usr/bin/python3
def magic_calculation(a, b):
    i = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
            else:
                i += (a ** b) / j
        except Exception:
            i = b + a
            break
    return i
