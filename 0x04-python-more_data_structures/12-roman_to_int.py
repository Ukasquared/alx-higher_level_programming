#!/usr/bin/python3

def roman_to_int(roman_string):
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman_string) == 0 or not isinstance(roman_string, str):
        return (0)

    result = 0
    temp_val = 0

    for i in range(len(roman_string) - 1, -1, -1):
        if roman_string[i] in rom_num.keys():
            value = rom_num[roman_string[i]]
            if value >= temp_val:
                result += value
            else:
                result -= value
            temp_val = value
        return (result)
