#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        if my_list:
            new_list = []
            for i in range(len(my_list)):
                if my_list[i] % 2 == 0:
                    new_list.insert(0, True)
                else:
                    new_list.insert(0, False)
            return new_list
