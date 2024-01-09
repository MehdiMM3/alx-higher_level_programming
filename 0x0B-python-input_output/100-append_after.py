#!/usr/bin/python3
"""Defining a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after each line containing a string for a file"""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
