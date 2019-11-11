
from init import *
class target(balls):
    # класс мишени
    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        super().__init__(rnd(600, 780), rnd(300, 550), rnd(2, 50))
        self.color = 'red'
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)
        self.live = 1
        self.vx = -5
        self.vy = -3
    def hit(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)
        canv.delete(self.id)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= 800 or self.x <=0 :
            self.vx =-self.vx
        if self.y >= 600 or self.y <=0:
            self.vy =-self.vy
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

