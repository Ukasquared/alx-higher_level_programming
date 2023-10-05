#!/usr/bin/python3
for num in range(0, 9):
    for num_2 in range((num + 1), 10):
        if num == 8 and num_2 == 9:
            print("{}{}".format(num, num_2))
            break
        else:
            print("{}{}".format(num, num_2), end=', ')
