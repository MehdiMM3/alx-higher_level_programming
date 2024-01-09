#!/usr/bin/python3
"""Defining a text read_file function."""


def read_file(filename=""):
    """Read file with utf-8."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
