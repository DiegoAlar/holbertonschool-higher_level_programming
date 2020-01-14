#!/usr/bin/python3
""" This module contains the function text_indentation """
def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of th    ese characters: ., ? and :
    """
    i = 0
    flag = True
    flag2 = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        while i < len(text):
            if text[i] is ' ' and flag2 is False:
                while flag is True and i < len(text):
                    i += 1
                    if text[i] is not ' ':
                        flag = False
                        i -= 1
            elif text[i] is '.' or text[i] is '?' or text[i] is ':':
                print("{:s}\n".format(text[i]))
                flag2 = True
            else:
                if flag2 is False:
                    print(text[i], end="")
                flag2 = False
            if flag is False and flag2 is False:
                flag = True
                print(text[i], end="")
                i += 1
            else:
                i += 1
