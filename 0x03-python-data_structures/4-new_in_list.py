#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # origin list copy
    new_list = my_list[:]

    # valid range check
    if 0 <= idx < len(new_list):
        # element replacement
        new_list[idx] = element

    return new_list
