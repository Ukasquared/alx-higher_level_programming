#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_dick = sorted(a_dictionary)
    for i in sort_dick:
        print("{}: {}".format(i, a_dictionary[i]))
