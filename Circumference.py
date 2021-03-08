class Circumference:
    def __init__(self, c, p):
        self.__c = c
        self.__p = p

    # calcolo raggio
    def calculateRadius(self):
        return self.__p.distance_from(self.__c)
