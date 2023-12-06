#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    resadd = add(a, b)
    ressub = sub(a, b)
    resmul = mul(a, b)
    resdiv = div(a, b)

    print(f"{a} + {b} = {resadd}")
    print(f"{a} - {b} = {ressub}")
    print(f"{a} * {b} = {resmul}")
    print(f"{a} / {b} = {resdiv}")
