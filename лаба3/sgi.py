from graph import *
from math import sin
from math import cos

points = list()
a = 40
dist_of_viu = a * 4
dist_of_pr = a * 2
alphaa = 0
cub = None


def get_ret_cub_lines_cords(alpha):
    cords = list()
    cords.append((a * cos(alpha) - a * sin(alpha) + dist_of_viu, a * sin(alpha) + a * cos(alpha), a / 2))
    cords.append((a * cos(alpha) + a * sin(alpha) + dist_of_viu, a * sin(alpha) - a * cos(alpha), a / 2))
    cords.append(-1 * (a * cos(alpha) + a * sin(alpha) + dist_of_viu, -1 * a * sin(alpha) - a * cos(alpha), a / 2))
    cords.append((a * cos(alpha) - a * sin(alpha) + dist_of_viu, a * sin(alpha) + a * cos(alpha), -a / 2))
    cords.append((a * cos(alpha) + a * sin(alpha) + dist_of_viu, a * sin(alpha) - a * cos(alpha), -a / 2))
    cords.append(-1 * (a * cos(alpha) + a * sin(alpha) + dist_of_viu, -a * sin(alpha) - a * cos(alpha), -a / 2))
    return cords


def get_pr_cub_cords(cords):
    pr_cords = list()
    for i in range(6):
        t = (cords[i+1][0] + dist_of_pr) / (cords[i+1][0] + dist_of_viu)
        pr_cords.append((dist_of_pr, cords[i][1] * (1 - t), cords[i][2] * (1 - t)))
    pr_cords.append(pr_cords[5])
    return pr_cords


def update():
    global alphaa
    global cub
    alphaa += 0.1
    deleteObject(cub)
    penColor("red")
    brushColor("red")
    cub = polygon(get_pr_cub_cords(get_ret_cub_lines_cords(alphaa)))


onTimer(update, 50)
run()
