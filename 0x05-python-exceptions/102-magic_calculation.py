#!/usr/bin/python3
def magic_calculation(a, b):
    i = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
            else:
                i += (a ** b) / j
            return i
        except Exception:
            i = b + a
            break
