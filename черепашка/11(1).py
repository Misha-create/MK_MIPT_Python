import turtle

turtle.shape('turtle')

def polygon (angle, length):
    for i in range(angle):
        turtle.forward(length)
        turtle.left(360/(360/angle))
    for i in range(angle):
        turtle.forward(length)
        turtle.right(360(360/angle)) 

   
turtle.left(90)
for j in range(int(input())):
    polygon(100+j*25, 60)
