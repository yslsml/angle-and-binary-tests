from math import pi
from draw import *
from functions import *

def main():
    bigPolygon = [Point(13, 4), Point(10, 9), Point(8, 9),  Point(5, 9),  Point(3, 7),
                   Point(1, 2), Point(1, 1), Point(12, 1), Point(13, 3)]

    smallPolygon = [Point(4, 4), Point(5, 5), Point(7, 5), Point(9, 6), Point(10, 6),
                                      Point(7, 3), Point(6, 4)]

    n = 7
    points = initPoints(bigPolygon, n)  # инициализация точек рандомными значениями

    for point in points:  # задаем направление движения точек и скорость
        alfa = random.uniform(0, 2*pi)  # случайное число с плавающей точкой
        speed = 0.8
        point.setDirection(Vector.getVector(alfa, speed))
        point.setSpeed(speed)

    mainTask(bigPolygon, smallPolygon, points)

main()