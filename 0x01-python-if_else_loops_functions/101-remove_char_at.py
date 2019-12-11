#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    if len(str) < n or n < 0:
        return (str)
    for i in range(0, n):
        str2 = str2 + str[i]
    for k in range(n + 1, len(str)):
        str2 = str2 + str[k]
    return (str2)
