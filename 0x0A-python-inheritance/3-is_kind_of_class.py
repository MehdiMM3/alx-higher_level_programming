#!/usr/bin/python3
"""Defining a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checking if an object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
