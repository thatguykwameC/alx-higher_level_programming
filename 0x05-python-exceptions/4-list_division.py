#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotient_list = []

    for i in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            quotient_list.append(quotient)

    return quotient_list
