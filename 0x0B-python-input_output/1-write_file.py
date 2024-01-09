#!/usr/bin/python3
"""Defining a file-writing function."""


def write_file(filename="", text=""):
    """Read the file with utf-8"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
