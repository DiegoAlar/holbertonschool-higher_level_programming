#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    arr = dir(hidden_4)
    for i in arr:
        if (i[0] != '_' and i[1] != '_'):
            print(i)
