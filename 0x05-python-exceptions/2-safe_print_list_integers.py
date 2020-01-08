#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    try:
        if x <= 0:
            print()
            return 0
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
            else:
                cont += 1
        print()
        return i + 1 - cont
    except (ValueError, TypeError):
        print()
