#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_List = []

    if my_list:
        for number in my_list:
            if number % 2 == 0:
                new_List.append(True)
            else:
                new_List.append(False)
        return new_List
