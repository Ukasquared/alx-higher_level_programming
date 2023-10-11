#!/usr/bin/python3
from sys import argv

# adds infinite numbers
if __name__ == "__main__":
    def inf_add():
        result = 0
        for i in argv[1:]:
            result += int(i)
        print(result)
inf_add()  # always call the function
