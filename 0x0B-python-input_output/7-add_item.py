#!/usr/bin/python3
"""task7"""
import sys

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

        arglist = list(sys.argv[1:])

    try:
        esdf = load_from_json_file("add_item.json")
    except Exception:
        esdf = []
    esdf.extend(arglist)
    save_to_json_file(esdf, "add_item.json")

