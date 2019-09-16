import turtle

turtle.shape('turtle')

def polygon (angle, l):
    for i in range(angle//2):
        turtle.forward(l)
        turtle.right(360/angle) 

big = int(input())
small = int(input())
n = int(input())
   
turtle.left(90)
for i in range(n):
    polygon(big, 1)
    polygon(small, 1)
