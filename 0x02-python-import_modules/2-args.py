#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    counter = len(sys.argv) - 1

    if counter == 0:
        print("0 arguements.")
    elif counter == 1:
        print("1 arguements:")
    else:
        print("{} arguements:".format(counter))
    for i in range(counter):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
