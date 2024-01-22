#!/usr/bin/python3
def magic_calculation(a, b):
    acc_result = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
            else:
                acc_result += (a**b) / j
        except Exception:
            acc_result = b + a
            break
    return acc_result
