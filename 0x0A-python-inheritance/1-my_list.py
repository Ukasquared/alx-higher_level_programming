#!/usr/bin/python3

"""module that injerits from list"""


class MyList(list):
    """ this class inherits
    the attrinutes and methods from my list """
    def print_sorted(self):
        print(sorted(self))

