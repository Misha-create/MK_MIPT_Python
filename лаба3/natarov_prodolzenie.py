from graph import *
from math import fabs
from math import cos
from math import sin
from math import pi
from time import sleep
import time

state = 0
usa = list()
obj = list()


def ellipse(xo, yo, a, b, color, angle):
    a = int(a)
    b = int(b)
    points = list()
    for i in range(-a * 10, a * 10, 1):
        xold = i / 10
        yold = (b ** 2 * (1 - (i / 10) ** 2 / a ** 2)) ** 0.5
        xnew = xo + xold * cos(angle) + yold * sin(angle)
        ynew = yo + yold * cos(angle) - xold * sin(angle)
        points.append((xnew, ynew))
    for i in range(a * 10, -a * 10, -1):
        xold = i / 10
        yold = -((b ** 2 * (1 - (i / 10) ** 2 / a ** 2)) ** 0.5)
        xnew = xo + xold * cos(angle) + yold * sin(angle)
        ynew = yo + yold * cos(angle) - xold * sin(angle)
        points.append((xnew, ynew))
    brushColor(color)
    return polygon(points)


def half_ellipse(xo, yo, a, b, color, angle):
    points = list()
    for i in range(-a * 10, a * 10, 1):
        xold = i / 10
        yold = (b ** 2 * (1 - (i / 10) ** 2 / a ** 2)) ** 0.5
        xnew = xo + xold * cos(angle) + yold * sin(angle)
        ynew = yo + yold * cos(angle) - xold * sin(angle)
        points.append((xnew, ynew))
    brushColor(color)
    polygon(points)


def planet():
    ellipse(350, 150, 100, 100, "white", -(pi / 8))
    ellipse(350, 150, 80, 100, "black", -(pi / 8))
    ellipse(350, 150, 300, 30, "gray", -(pi / 8))
    ellipse(350, 150, 200, 27, "black", -(pi / 8))
    ellipse(350, 150, 190, 24, "white", -(pi / 8))
    ellipse(350, 150, 150, 21, "black", -(pi / 8))
    half_ellipse(350, 150, 100, 100, "white", pi - (pi / 8))
    half_ellipse(350, 150, 80, 100, "black", pi - (pi / 8))


def astronaut(x, y, k, color):
    penColor(color)
    obj.append(ellipse(x, y, 12 / k, 12 / k, color, 0))
    obj.append(ellipse(x + 1 / k, y - 1 / k, 10 / k, 9 / k, "black", 0))

    obj.append(ellipse(x, y + 33 / k, 12 / k, 22 / k, color, 0))

    obj.append(ellipse(
        x + 17 / k,
        y + 53 / k,
        14 / k, 8 / k,
        color,
        -(pi / 6)
    ))
    obj.append(ellipse(
        x + 29 / k,
        y + 66 / k,
        10 / k,
        8 / k,
        color,
        -(pi / 2)
    ))
    obj.append(ellipse(x + 37 / k, y + 78 / k, 10 / k, 6 / k, color, 0))

    obj.append(ellipse(x - 12 / k, y + 60 / k, 14 / k, 8 / k, color, (pi / 3)))
    obj.append(ellipse(
        x - 10 / k,
        y + 76 / k,
        10 / k,
        8 / k,
        color,
        -(pi / 3)
    ))
    obj.append(ellipse(x - 10 / k, y + 90 / k, 10 / k, 6 / k, color, (pi / 6)))

    obj.append(ellipse(x + 16 / k, y + 16 / k, 7 / k, 7 / k, color, 0))
    obj.append(ellipse(x + 26 / k, y + 10 / k, 5 / k, 5 / k, color, 0))
    obj.append(ellipse(x + 32 / k, y + 4 / k, 5 / k, 5 / k, color, 0))

    obj.append(ellipse(x - 16 / k, y + 16 / k, 7 / k, 7 / k, color, 0))
    obj.append(ellipse(x - 26 / k, y + 22 / k, 5 / k, 5 / k, color, 0))
    obj.append(ellipse(x - 32 / k, y + 28 / k, 5 / k, 5 / k, color, 0))


def bookcase():
    brushColor(139, 69, 19)
    penColor(139, 69, 19)
    rectangle(200, 440, 500, 600)
    brushColor(102, 51, 0)
    penColor(102, 51, 0)
    rectangle(200, 440, 500, 450)
    rectangle(200, 490, 500, 500)
    rectangle(200, 540, 500, 550)
    rectangle(200, 590, 500, 600)


def book(xo, yo, x, y, color):
    brushColor(color)
    penColor(color)
    rectangle(xo, yo, x, y)


def USA(x, y):
    penSize(0.001)
    brushColor("red")
    penColor("red")
    usa.append(rectangle(x, y, x + 80, y + 52))
    penColor("white")
    brushColor("white")
    for i in range(1, 12, 2):
        usa.append(rectangle(x, y + 4 * i, x + 80, y + 4 * i + 3))
    penColor("blue")
    brushColor("blue")
    usa.append(rectangle(x, y, x + 35, y + 28))
    for j in range(0, 3, 1):
        for i in range(0, 3, 1):
            star(x + i * 10 + 6, y + j * 10 + 6, 3, "white")
    penColor("white")
    usa.append(line(x, y, x, y + 150))


def star(x, y, r, color):
    penColor(color)
    moveTo(x, y - r)
    usa.append(lineTo(x + r * sin(pi / 5), y + r * cos(pi / 5)))
    usa.append(lineTo(x - r * sin(2 * pi / 5), y - r * cos(2 * pi / 5)))
    usa.append(lineTo(x + r * sin(2 * pi / 5), y - r * cos(2 * pi / 5)))
    usa.append(lineTo(x - r * sin(pi / 5), y + r * cos(pi / 5)))
    usa.append(lineTo(x, y - r))


def delete():
    for i in obj:
        deleteObject(i)
    obj.clear()


flag_one = False
flag_two = False
k = 1.1


def up():
    global flag_one
    global flag_two
    global obj
    global k
    if not flag_two and yCoord(obj[0]) <= 100:
        USA(320, 50)
        flag_one = True
    if not flag_one:
        for i in obj:
            moveObjectBy(i, 5, -5)
    elif not flag_two:
        ellipse(
            350,
            150,
            int(300 - 300 / k),
            int(600 - 500 / k),
            "yellow",
            pi - (pi / 8)
        )
        k = k + 0.5
        if k > 10.0:
            flag_two = True
            brushColor("yellow")
            penColor("yellow")
            rectangle(0, 0, 600, 600)
            astronaut(-50, 400, 1, "red")
    else:
        if yCoord(obj[10]) <= 5:
            close()
        for i in obj:
            moveObjectBy(i, xCoord(i) * 1 / 40 + 2, -yCoord(i) * 1 / 60)


brushColor("Black")
rectangle(0, 0, 500, 600)
planet()
bookcase()
book(200, 450, 210, 490, "red")
book(210, 460, 220, 490, "green")
book(220, 470, 230, 490, "blue")
book(250, 490, 270, 450, "yellow")
astronaut(50, 350, 1, "gray")
onTimer(up, 50)
run()
time.sleep(3)
