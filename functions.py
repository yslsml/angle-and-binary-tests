from math import floor
from Point import Point
from Vector import Vector
import random

def initPoints(polygon, n) -> list:
    min = getMinPoint(polygon)
    max = getMaxPoint(polygon)
    X = [random.randint(min.x, max.x) for _ in range(n)]
    Y = [random.randint(min.y, max.y) for _ in range(n)]
    points = []
    for i in range(len(X)):
        el = Point(X[i], Y[i])
        while binaryTest(polygon, el)['flag'] == False:
            el.x = random.randint(min.x, max.x)
            el.y = random.randint(min.y, max.y)
        points.append(el)
    return points

def det(a, b, c, d):
    return a * d - b * c

def next(i, n):
    return i + 1 if i < n - 1 else 0

def areIntersect(P1: Point, P2: Point, P3: Point, P4: Point) -> bool:
    d1 = det(P4.x - P3.x, P4.y - P3.y, P1.x - P3.x, P1.y - P3.y)
    d2 = det(P4.x - P3.x, P4.y - P3.y, P2.x - P3.x, P2.y - P3.y)
    d3 = det(P2.x - P1.x, P2.y - P1.y, P3.x - P1.x, P3.y - P1.y)
    d4 = det(P2.x - P1.x, P2.y - P1.y, P4.x - P1.x, P4.y - P1.y)

    c1 = (P3.x - P1.x) * (P4.x - P1.x) + (P3.y - P1.y) * (P4.y - P1.y)
    c2 = (P3.x - P2.x) * (P4.x - P2.x) + (P3.y - P2.y) * (P4.y - P2.y)
    c3 = (P1.x - P3.x) * (P2.x - P3.x) + (P1.y - P3.y) * (P2.y - P3.y)
    c4 = (P1.x - P4.x) * (P2.x - P4.x) + (P1.y - P4.y) * (P2.y - P4.y)

    if d1 == d2 and d2 == d3 and d3 == d4 and d4 == 0:
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0:
            return False
        else:
            return True
    elif d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False

def determinant(p, p1, p2):  # p относительно p1p2
    return (p2.x - p1.x) * (p.y - p1.y) - (p.x - p1.x) * (p2.y - p1.y)

def getMinPoint(polygon):
    minX = polygon[0].x
    minY = polygon[0].y
    for i in range(0, len(polygon)):
        if polygon[i].x < minX:
            minX = polygon[i].x
        if polygon[i].y < minY:
            minY = polygon[i].y
    return Point(minX, minY)

def getMaxPoint(polygon):
    maxX = polygon[0].x
    maxY = polygon[0].y
    for i in range(0, len(polygon)):
        if polygon[i].x > maxX:
            maxX = polygon[i].x
        if polygon[i].y > maxY:
            maxY = polygon[i].y
    return Point(maxX, maxY)

def gabaritTest(p0, pMin, pMax) -> bool:
    if p0.x > pMax.x or p0.y > pMax.y or p0.x < pMin.x or p0.y < pMin.y:
        return False  # не в многоугольнике
    else:
        return True  # в многоугольнике

def checkPositionOfPoint(p0, p1, p2):  # p0 относительно p1p2
    d = determinant(p0, p1, p2)
    if d > 0:
        return 1  # левее
    elif d < 0:
        return -1  # правее
    else:
        return 0  # на прямой

def angleTest(polygon, p0):  # положение точки относительно простого (маленького) многоугольника
    if gabaritTest(p0, getMinPoint(polygon), getMaxPoint(polygon)) == False:
        return False  # не в многоугольнике

    n = len(polygon)
    s = 0  # счетчик суммы октанов
    for i in range(0, n):
        r1 = oct(p0, polygon[i])  # октант относительно и-той
        r2 = oct(p0, polygon[next(i, n)])  # октант относительно и+1-ой
        r = correction(r2 - r1, polygon[i], polygon[next(i, n)], p0)  # коррекция
        if r == "Точка лежит на стороне":
            return False
        s += r
    if s == 0:  # не в многоугольнике
        return False
    elif s == 8 or s == -8:  # в многоугольнике
        return True
    else:
        return "Ошибка в алгоритме"

def oct(p1, p2):
    x = p2.x - p1.x
    y = p2.y - p1.y
    if 0 <= y < x:
        return 1
    elif 0 < x <= y:
        return 2
    elif 0 <= -x < y:
        return 3
    elif 0 < y <= -x:
        return 4
    elif 0 <= -y < -x:
        return 5
    elif 0 < -x <= -y:
        return 6
    elif 0 <= x < -y:
        return 7
    elif 0 < -y <= x:
        return 8

def correction(r, p1, p2, p0):  # r = дельта i-тое, р1 = рi-тое, р2 = р(i+1)-ое, р0 = р0
    if r > 4:
        return r - 8
    elif r < -4:
        return r + 8
    elif r == 4 or r == -4:
        d = checkPositionOfPoint(p2, p0, p1)
        if d > 0:
            return 4
        elif d < 0:
            return -4
        elif d == 0:
            return "Точка лежит на стороне"
    else:
        return r

def binaryTest(polygon, p0):  # находится ли р0 в многоугольнике (выпуклом)
    n = len(polygon)

    if determinant(p0, polygon[0], polygon[1]) * determinant(polygon[n-1], polygon[0], polygon[1]) < 0:
        res = {'flag': False, 'side': [polygon[0], polygon[1]]}
        return res
    elif determinant(p0, polygon[0], polygon[n-1]) * determinant(polygon[1], polygon[0], polygon[n-1]) < 0:
        res = {'flag': False, 'side': [polygon[0], polygon[n - 1]]}
        return res

    start = 1
    end = n - 1
    while end - start > 1:
        sep = floor((start + end) / 2)
        if determinant(polygon[0], polygon[sep], p0) < 0:
            end = sep
        else:
            start = sep

    if areIntersect(polygon[0], p0, polygon[start], polygon[end]):
        res = {'flag': False, 'side': [polygon[start], polygon[end]]}
        return res
    else:
        res = {'flag': True}
        return res

def reflection(p, coords):
    # newDir = (2 * (scalarProducot(a, b) / scalarProduct(b, b)) * b) - a
    a = p.direction  # предыдущее направление
    b = Vector(coords[0], coords[1])  # сторона многоугольника

    scalar = 2 * (Vector.scalarProduct(a, b) / Vector.scalarProduct(b, b))
    tmpVector = Vector.multiplyOnScalar(b, scalar)
    newDirection = Vector.subtract(tmpVector, a)
    return newDirection

def sumSpeed(points):
    s = 0
    for p in points:
        s += p.speed
    return s