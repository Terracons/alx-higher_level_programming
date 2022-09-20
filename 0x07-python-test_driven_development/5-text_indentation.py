#!/usr/bin/python3
"""
text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """text_indentation will add two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delimeter in ".:?":
        text = (delimeter + "\n\n").join(
            [line.strip(" ") for line in text.split(delimeter)])

    print("{}".format(text), end="")
