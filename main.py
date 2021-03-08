from Point import Point
from Straight import Straight
from Circumference import Circumference

# creazione punto, retta, circonferenza
point1 = Point(2, 20)
point2 = Point(2, 10)
straight = Straight(point1, 1);
circumference = Circumference(point1, point2)

# prova metodi
print(point1.mid_point(point2))
print(point1.distance_from(point2))
print(straight.distance_from(point1))
print(straight.calculateQ())
print(circumference.calculateRadius())
