#!/usr/bin/python3
"""Defining a Python class to json function."""


def class_to_json(obj):
    """Return the dictionary represntation of data structure."""
    return obj.__dict__
