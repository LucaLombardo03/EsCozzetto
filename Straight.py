import math

from Point import Point;


class Straight:

    def __init__(self, p, m):
        self.__p = p
        self.__m = m

    # distanza tra retta e punto
    def distance_from(self, p):
        numerator = p.y - (self.__m * p.x);
        if numerator < 0:
            numerator = -numerator;
        return numerator / math.sqrt(1 + self.__m * self.__m)

    # calcolo coefficiente q
    def calculateQ(self):
        return self.__m * (-self.__p.x + self.__p.y)

    # intersezione tra due retta
    def intersection(self, line):
        x = self.__calculateQ() - line.calculateQ() / (self.__m - line.m)
        return Point(x, self.__m * x + self.__calculateQ())
