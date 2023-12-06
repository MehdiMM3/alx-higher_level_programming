#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    vlm = 0
    kym = None
    for k, v in a_dictionary.items():
        if v > vlm:
            vlm = v
            kym = k
    return kym
