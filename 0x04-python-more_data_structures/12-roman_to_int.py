#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    ftot = 0
    g = 0
    dg = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for r in reversed(roman_string):
        g = dg[r]
        ftot += g if ftot < g * 5 else -g
    return ftot
