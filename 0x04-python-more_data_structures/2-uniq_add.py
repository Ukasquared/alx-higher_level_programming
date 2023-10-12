#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    new_list = list(set(my_list))
    for index in new_list:
        result += index
    return result
