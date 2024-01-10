#!/usr/bin/python3
"""Defining a class-checking function."""


def is_same_class(obj, a_class):
    """Checking if an object is an instance of class"""
    if type(obj) == a_class:
        return True
    return False
