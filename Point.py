import math


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # punto medio tra due punti
    def mid_point(self, other):
        return Point((self.__x + other.__x) / 2, (self.__y + other.__y) / 2)

    # distanza tra due punti
    def distance_from(self, other):
        return math.sqrt(
            (self.__x - other.__x) * (self.__x - other.__x) + (self.__y - other.__y) * (self.__y - other.__y))
