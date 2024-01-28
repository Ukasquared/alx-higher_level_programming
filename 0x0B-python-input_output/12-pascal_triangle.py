#!/usr/bin/python3
""" pascal triangle module"""

def pascal_triangle(n):
    """ pascal triangle """
    aggr_list = []
    for i in range(n):
        sub_list = []
        if i == 0:
            sub_list = [1]
            aggr_list.append(sub_list)
        if i == 1:
            sub_list = [1, 1]
            aggr_list.append(sub_list)
        if i > 1:
            temp_list = aggr_list[i - 1]
            temp_len = len(temp_list)
            for j in range(temp_len):
                if j == 0:
                    sub_list.append(temp_list[j])
                elif j == temp_len - 1:
                    sub_list.append(temp_list[j - 1] + temp_list[j])
                    sub_list.append(temp_list[j])
                else:
                    sub_list.append(temp_list[j - 1] + temp_list[j])
            aggr_list.append(sub_list)
    return aggr_list