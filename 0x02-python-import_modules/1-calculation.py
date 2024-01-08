#!/usr/bin/python3

# Import the functions: add, sub, mul, div
from calculator_1 import add, sub, mul, div

a = 10
b = 5

# This code should not run when this file is imported
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
