#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_let = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_nums = []
    subs = 0
    suma = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for s in roman_string:
        list((map(lambda x: list_nums.append(rom_let[x]) if x == s else 0, rom_let)))
    for l in range(len(list_nums)):
        if (l != (len(list_nums) - 1)):
            if ((list_nums[l] == 1) and (list_nums[l + 1] == 10)):
                subs += 1
            elif ((list_nums[l] == 1) and (list_nums[l + 1] == 5)):
                subs += 1
            elif ((list_nums[l] == 10) and (list_nums[l + 1] == 50)):
                subs += 10
            elif ((list_nums[l] == 100) and (list_nums[l + 1] == 1000)):
                subs += 100
            elif ((list_nums[l] == 10) and (list_nums[l + 1] == 100)):
                subs += 10
    suma = sum(s for s in list_nums) - subs
    return suma - subs
