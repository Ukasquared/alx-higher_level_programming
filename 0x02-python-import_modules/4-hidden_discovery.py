#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    def name_s():
        # list of names in module
        names = dir(hidden_4)
        for name in names:
            if name[:2] in names != "__":
                print("{}".format(names))
