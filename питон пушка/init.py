from random import randrange as rnd, choice
from tkinter import *
import math
import time
root = Tk()
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
root.geometry('800x600')
fr = Frame(root)
ballss = []
class balls():
    # параметры шара: координаты, радиус, ускорение по y, сопротивление среды по x, упругость при отскоке
    def __init__(self, x, y, r, g=0, k=0, n=0):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.k = k
        self.n = n

class ball(balls):
    # класс пули
    def __init__(self, x=40, y=450, r=10, g=1.2, k=0.99, n=5):
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        super().__init__(x, y, r, g, k, n)
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.live = 30

    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        if self.y <= 500:
            self.vy -= self.g
            self.y -= self.vy
            self.x += self.vx
            self.vx *= self.k
            self.set_coords()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / self.n
                self.vx = self.vx / self.n
                self.y = 499
            if self.live < 0:
                ballss.pop(ballss.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = -self.vx / 2
            self.x = 779

    def hittest(self, ob):
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False

