from tkinter import *
from random import randrange as rnd, choice
import time

balls = list()
angels = list()
steps = list()
free_points = list()
for i in range(100, 800):
    for j in range(100, 550):
        free_points.append((i, j))
saved_free_points = free_points
colors = ['white', "gray"]
wateing_time = 1000
goals = 0
for i in range(100):
    angels.append(-2 + i / 25)
    steps.append(-2 + i / 25)
root = Tk()
root.geometry('800x600')
canvas = Canvas(root, bg='black')
canvas.pack(fill=BOTH, expand=1)


class Ball(object):
    def __init__(self):
        self.color = choice(colors)
        self.x = choice(free_points)[0]
        self.y = choice(free_points)[1]
        self.r = rnd(5, 10)
        self.m = self.r / 10
        self.dx = choice(steps)
        self.dy = choice(angels)
        self.obj = None

    def delete(self):
        canvas.delete(self.obj)
        self.obj = None

    def move(self):
        self.x += self.dx
        self.y += self.dy
        canvas.move(self.obj, self.dx, self.dy)

    def create(self):
        self.obj = canvas.create_oval(self.x - self.r,
                                      self.y - self.r,
                                      self.x + self.r,
                                      self.y + self.r,
                                      fill=self.color, width=0)


for i in range(20):
    balls.append(Ball())


def click(event):
    global goals
    for i in range(len(balls)):
        if (balls[i].x + balls[i].r >= event.x >= balls[i].x - balls[i].r) and (
                balls[i].y + balls[i].r >= event.y >= balls[i].r - balls[i].y):
            goals += 1
            canvas.delete(balls[i].obj)
            balls.pop(i)
            break


def delete_balls():
    canvas.delete(ALL)


def create_balls():
    global balls
    for i in range(len(balls)):
        balls[i] = Ball()
        balls[i].create()


def mov_balls():
    global balls
    for i in range(len(balls)):
        if balls[i].x + balls[i].r >= 800 or balls[i].x + balls[i].r <= 50:
            balls[i].dx = -balls[i].dx
        if balls[i].y + balls[i].r >= 550 or balls[i].y + balls[i].r <= 50:
            balls[i].dy = -balls[i].dy
        for q in range(i, len(balls)):
            if abs(balls[q].x - balls[i].x) <= abs(balls[q].r + balls[i].r - 2) and abs(balls[q].y - balls[i].y) <= abs(
                    balls[q].r + balls[i].r - 2) and i != q:
                r = balls[q].dx
                balls[q].dx = balls[i].dx
                balls[i].dx = r
                r = balls[q].dy
                balls[q].dy = balls[i].dy
                balls[i].dy = r

    for i in range(len(balls)):
        balls[i].move()


def get_text():
    if goals < 5:
        canvas.create_text(600, 300, text=str(goals) + "/20 был бы ты человеком", anchor=SE, fill="grey",
                           font="Verdana 24")
    elif goals < 10:
        canvas.create_text(600, 300, text=str(goals) + "/20 уд 3", anchor=SE, fill="grey", font="Verdana 24")
    else:
        canvas.create_text(600, 300, text=str(goals) + "/20 c этим можно работать", anchor=SE, fill="grey",
                           font="Verdana 24")


def main():
    for i in range(10):
        root.after(i * wateing_time + 1, create_balls)
        root.after((i + 1) * wateing_time, delete_balls)
        for j in range(int(wateing_time / 10)):
            root.after(i * wateing_time + 10 * j + 1, mov_balls)
    root.after(10 * wateing_time + 20, get_text)


main()
canvas.bind('<Button-1>', click)
mainloop()
