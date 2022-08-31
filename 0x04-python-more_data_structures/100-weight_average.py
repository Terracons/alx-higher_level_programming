#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for tupp in my_list:
        average += tupp[0] * tupp[1]
        div += tupp[1]
    return float(average / div)
