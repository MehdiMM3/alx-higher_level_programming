#!/usr/bin/python3
"""Algorithms"""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted ints."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
