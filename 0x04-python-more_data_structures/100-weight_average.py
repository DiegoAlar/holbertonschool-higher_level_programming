#!/usr/bin/python3
def weight_average(my_list=[]):
        if my_list:
            add = 0
            div = 0
            for i in my_list:
                add += i[0] * i[1]
                div += i[1]
            return add / div
        else:
            return 0
