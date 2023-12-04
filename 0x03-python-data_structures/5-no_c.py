#!/usr/bin/env python3
def no_c(my_string):
    # string creation
    new_string = ''.join(char for char in my_string if char.lower() not in {'c', 'C'})
    return new_string
