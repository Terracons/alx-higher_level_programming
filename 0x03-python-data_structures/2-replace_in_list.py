#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if there is out of range
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
