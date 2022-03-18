import matplotlib.pyplot as plt
from functions import *

def drawPolygon(points: list):
    for i in range(0, len(points)):
        if i + 1 == len(points):
            k = 0  # k - индекс последней точки
        else:
            k = i + 1
        plt.plot([points[i].x, points[k].x], [points[i].y, points[k].y])

def mainTask(P, Q, points):  # P - большой, Q - маленький,
    plt.ion()  #включение интерактивного режима для анимации

    s = sumSpeed(points)
    while s:
        plt.clf()  # очистить текущую фигуру
        s = sumSpeed(points)
        drawPolygon(P)
        drawPolygon(Q)

        for p in points:
            angleFlag = angleTest(Q, p.nextState())
            binaryFlag = binaryTest(P, p.nextState())['flag']

            if binaryFlag == False:  # следующее состоние точки не в выпуклом многоугольнике
                plt.scatter(p.x, p.y)  # рисует точку
                sideCoords = binaryTest(P, p.nextState())['side']
                newDir = reflection(p, sideCoords)
                p.direction = newDir
            elif angleFlag == True:  # следующее состоние точки в простом многоугольнике
                p.setSpeed(0)
            else:
                p.next()  # точка движется дальше по направлению
                plt.scatter(p.x, p.y)  # рисует точку

        # обновление графика
        plt.draw()
        plt.gcf().canvas.flush_events()
        plt.pause(0.0000001)

    plt.ioff()  #выключение интерактивного режима
    plt.show()