#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    argvLength = len(argv)

    if (argvLength == 1):
        print("{:d} arguments".format(argvLength - 1))
    if (argvLength == 2):
        print("{:d} argument:".format(argvLength - 1))
    if (argvLength > 2):
        print("{:d} arguments:".format(argvLength - 1))
    for i in range(argvLength):
        print("{:d}: {:s}".format(i+1, argv[i]))
