#!/usr/bin/python3
def max_integer(my_list=[]):
        if my_list:
            mayor = my_list[0]
            for i in range(len(my_list) - 1):
                    if mayor < my_list[i]:
                        mayor = my_list[i]
            return mayor

        else:
            return None
