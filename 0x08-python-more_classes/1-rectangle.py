#!/usr/bin/python3
""" Rectangle class
This mode contain empty python class

Usage example:
    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
"""


class Rectangle:
    """
    docsting of class Rectangle
    Attribute:
        width: an integer which represent the width
        of rectangule
        height: also an integer that represent the
        height of rectangule.

    """

    def __init__(self, width=0, height=0):
        """ An object construtor method
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        this is getter for the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        thsis setter for width"
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height attribte
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
