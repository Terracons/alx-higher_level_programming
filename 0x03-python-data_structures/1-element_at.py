#!/usr/bin/python3
def element_at(my_list, idx):
    # Check for negative and out of range index
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
