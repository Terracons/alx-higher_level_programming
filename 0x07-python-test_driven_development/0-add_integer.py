#!/usr/bin/python3
"""
add_integer:  
    this program check if parameter
    are int and return sum
"""

def add_integer(a, b=98):
    """
    checks if param is int and return sum
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    
    if type(a) != int:
        raise TypeError('a must be an integer')
    elif type(b) != int:
        raise TypeError('b must be integer')
    else:
        return a + b