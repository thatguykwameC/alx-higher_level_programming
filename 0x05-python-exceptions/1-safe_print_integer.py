#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(f"{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True