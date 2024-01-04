#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arg_count = len(argv) - 1

    if arg_count < 1:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:".format(arg_count))
    else:
        print("{} arguments:".format(arg_count))
    for i in range(counter):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
