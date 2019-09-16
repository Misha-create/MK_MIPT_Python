import turtle

turtle.shape('turtle')
length = 10
square = 90
step = 30
def square(length):
	for i in range(4):
		turtle.forward(length)
		turtle.left(90)
for i in range(10):
	square(length)
	turtle.penup()
	turtle.right(90)
	turtle.forward(step)
	turtle.right(90)
	turtle.forward(step)
	turtle.right(180)
	turtle.down()
	length+=2*step
input()
