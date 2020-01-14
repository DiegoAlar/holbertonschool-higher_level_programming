#!/usr/bin/python3
""" This module contains the function text_indentation """
def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of th    ese characters: ., ? and :
    """
    i = 0
    flag = True
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        while i < len(text):
            if text[i] is ' ':
                while flag is True and i < len(text):
                    i += 1
                    if text[i] is not ' ':
                        flag = False
            elif text[i] is '.' or text[i] is '?' or text[i] is ':':
                print("{:s}\n".format(text[i]))
                if text[i] is not '.' and text[i] is not '?' and\
                        text[i] is not ':':
                    i = i + 1
            else:
                print(text[i], end="")
            if flag is False:
                print(" ", end="")
                flag = True
            else:
                i += 1
