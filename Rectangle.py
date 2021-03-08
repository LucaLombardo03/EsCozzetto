class Rectangle:

    def __init__(self, p, p1):
        self.__p = p
        self.__p1 = p1

    def calculateHigh(self):
        if self.__p.y - self.__p1.y < 0:
            return -(self.__p.y - self.__p1.y < 0)
        return self.__p.y - self.__p1.y < 0

    def calculateWidth(self):
        if self.__p.__x - self.__p1.x < 0:
            return -(self.__p.x - self.__p1.x < 0)
        return self.__p.x - self.__p1.x < 0

    # calcolo perimetro
    def calculatePerimeter(self):
        return (self.__calcolateHigh * 2) + (self.__calculateWidth * 2)

    # calcolo area
    def calculateArea(self):
        return self.__calcolateHigh * self.__calculateWidth