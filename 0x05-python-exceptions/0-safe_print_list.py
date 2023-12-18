#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        rfgg = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            rfgg += 1
        print()
        return rfgg
    except IndexError:
        print()
        return rfgg
