import turtle

turtle.shape('turtle')
n=12
length = 30
for i in range(n):
	turtle.forward(length)
	turtle.stamp()
	turtle.left(180)
	turtle.penup()
	turtle.forward(length)
	turtle.pendown()
	turtle.left(180 + 360/n)
