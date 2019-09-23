from graph import *
from math import fabs
def draw_built(x,y,x1,y1,color):
    penColor(color)
    brushColor(color)
    rectangle(x, y, x1, y1)
def draw_car(x,y,color):
    brushColor(color)
    penColor(color)
    rectangle(x, y, x+250, y+30)
    rectangle(x+100,y,x+220,y-25)
    brushColor("white")
    penColor("white")
    rectangle(x+120,y-5,x+150,y-20)
    rectangle(x+170,y-5,x+200,y-20)
    brushColor("orange")
    penColor("orange")
    circle(x+60, y+30, 15)
    circle(x+200, y+30, 15)
def fence():
    brushColor("white")
    penColor("white")
    length=5
    x=0
    for i in range(34):
        polygon([(x,400),(x+length,400),(x+3*length,350),(x+2*length,350),(x,400)])
        x = x + length*3
def draw_all_car(x,y):
    draw_car(x-21,y-15,"orange")
    draw_car(x-14,y-10,(229, 240, 26))
    draw_car(x-7,y-5,"orange")
    draw_car(x,y,"yellow")
    penColor("yellow")
    brushColor("white")
    polygon([(x-21+100,y-15),(x-21+100,y-15-25),(x+100,y-25),(x+100,y),(x-21+100,y-15)])
def draw_ellips(a,b,x,y,color):
    points = list()
    moveTo(x-a/2)
    for i in range((x-a)*10,(x+a)*10,1):
        xi=i/10
        yi=y+(b**2*(1-(i/10-x)**2/a**2))**0.5
        points.append((xi,yi))
    brushColor(color)
    penColor(color)
    polygon(points)
def draw_all_ellips():
    draw_built(0,400,500,600,(84, 214, 94))
    draw_ellips(500,200,0,407,(195, 212, 15))
    draw_ellips(500,100,0,407,(196, 185, 31))
    draw_ellips(500,50,0,407,(84, 214, 94))
def draw_all_builts():
    draw_built(100,0,160,350,"yellow")
    draw_built(190,0,220,350,"yellow")
    draw_built(250,0,300,350,"yellow")
    draw_built(350,0,440,350,"yellow")
    draw_built(0,0,60,350,"yellow")
    for i in range(71):
        draw_built(0,5*i,600,5*i+2,"white")
    draw_built(20,140,230,400,(255,255,0))
    for i in range(22):
        draw_built(20+i*10,140,20+i*10+6,400,"white")
    draw_built(0,350,500,400,(255,255,0))
    draw_built(175,50,425,80,"yellow")
    draw_built(290,80,310,400,"yellow")
    draw_built(0,60,600,70,"yellow")
    draw_built(0,400,600,410,"orange")
    draw_built(0,340,600,350,"orange")
    fence()
draw_all_ellips()
draw_all_builts()
draw_all_car(200,480)
run()
