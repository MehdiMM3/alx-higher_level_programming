#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rfc in matrix:
        for x, y in enumerate(rfc):
            if x == len(rfc) - 1:
                print("{:d}".format(y), end="")
            else:
                print("{:d}".format(y), end=" ")
        print()
