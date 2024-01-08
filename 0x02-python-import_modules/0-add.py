#!/usr/bin/python3
# Import the add function
from task import add

a = 1
b = 2

# This code should not run when this file is imported
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}". format(a, b, add(a, b)))
