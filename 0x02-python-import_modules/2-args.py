#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arg = sys.argv[1:]
    arg_count = len(arg)

    if arg_count == 0:
        print("0 arguments.")
    else:
        if arg_count == 1:
            print("{} argument:\n{}: {}".format(arg_count, arg_count, arg[0]))
        else:
            print("{} arguments:".format(arg_count))
            for i in range(arg_count):
                print("{}: {}".format((i + 1), arg[i]))
