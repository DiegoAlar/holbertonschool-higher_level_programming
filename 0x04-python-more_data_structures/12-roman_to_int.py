#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_let = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    l_n = []
    subs = 0
    suma = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for s in roman_string:
        list((map(lambda x: l_n.append(rom_let[x]) if x == s else 0, rom_let)))
    for l in range(len(l_n)):
        if (l != (len(l_n) - 1)):
            if ((l_n[l] == 1) and (l_n[l + 1] == 10)):
                subs += 1
            elif ((l_n[l] == 1) and (l_n[l + 1] == 5)):
                subs += 1
            elif ((l_n[l] == 10) and (l_n[l + 1] == 50)):
                subs += 10
            elif ((l_n[l] == 100) and (l_n[l + 1] == 1000)):
                subs += 100
            elif ((l_n[l] == 10) and (l_n[l + 1] == 100)):
                subs += 10
    suma = sum(s for s in l_n) - subs
    return suma - subs
