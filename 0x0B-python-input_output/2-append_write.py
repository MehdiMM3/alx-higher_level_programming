#!/usr/bin/python3
"""Defining a file-appending function."""


def append_write(filename="", text=""):
    """append a file with utf-8"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

