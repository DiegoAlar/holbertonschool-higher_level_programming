#!/usr/bin/python3
for i in range(0, 9):
    for k in range(0, 10):
        if i < k:
            if i == 8 and k == 9:
                print("{}{}".format(i, k))
                break
            else:
                print("{}{}, ".format(i, k), end='')
