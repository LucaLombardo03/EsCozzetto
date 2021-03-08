class Triangle:

    def __init__(self, p, p1, p2):
        self._p = p
        self.__p1 = p1
        self.__p2 = p2

    # calcolo perimetro
    def calculatePerimeter(self):
        return self.__p.distance_from(self.__p1) + self.__p1.distance_from(self.__p2) + self.__p2.distance_from(self.__p)

    # calcolo area
    def calculateArea(self):
        if ((self.__p1.y - self.__p.y) * (self.__p2.x - self.__p1.x) + (self.__p1.y - self.__p2.y) * (
                self.__p.x - self.__p.x)):
            return (-(self.__p1.y - self.__p.y) * (self.__p2.x - self.__p1.x) + (self.__p1.y - self.__p2.y) * (
                        self.__p.x - self.__p.x)) / 2
        return ((self.__p1.y - self.__p.y) * (self.__p2.x - self.__p1.x) + (self.__p1.y - self.__p2.y) * (
                    self.__p.x - self.__p.x)) / 2
