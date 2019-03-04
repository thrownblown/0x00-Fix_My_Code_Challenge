#!/usr/bin/python3
"""
Area of the square
"""


class Square:
    """ Area of the square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Area of the square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Area of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Area of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Area of the square """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
