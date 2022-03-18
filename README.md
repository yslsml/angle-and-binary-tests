# Задание
Дано:
P = {p1(x1, y1), p2(x2, y2), … ,pn(xn, yn)} – простой многоугольник;
Q = {q1(x1, y1), q2(x2, y2), … ,qm(xm, ym)} – выпуклый многоугольник;
Многоугольник P находится внутри многоугольника Q. Между этими
многоугольниками (внутри Q и снаружи P) заданы k точек множества S
(например, см. рисунок). Создать анимацию движения точек S внутри
многоугольника Q с отражением от его стенок. При попадании точки внутрь
многоугольника P скорость ее движения обнуляется.
При выполнении задания должны быть реализованы следующие алгоритмы:
- “угловой тест” через октаны для определения положения точки
относительно простого многоугольника;
- “бинарный тест” для определения положения точки относительно
выпуклого многоугольника. 

# Task
Given:
P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} is a simple polygon;
Q = {q1(x1, y1), q2(x2, y2), … ,qm(xm, ym)} – convex polygon;
The polygon P is inside the polygon Q. Between these
polygons (inside Q and outside P), k points of the set S
are given (for example, see the figure). Create an animation of the movement of points S inside
the polygon Q with reflection from its walls. When a point gets inside
the polygon P, its velocity is reset to zero.
When performing the task, the following algorithms must be implemented:
- "angular test" through octanes to determine the position of a point
relative to a simple polygon;
- "binary test" to determine the position of a point relative
to a convex polygon.
