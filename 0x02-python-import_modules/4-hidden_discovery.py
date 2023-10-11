#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    def name_s():
        # list of names in module
        names = dir(hidden_4)
        #sort the list
        names_sort = sorted(names)
        for name in names_sort:
            if name[:2] in names_sort == "__":
                continue
            else:
                print("{}".format(names_sort))
