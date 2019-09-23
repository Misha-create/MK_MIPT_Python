import turtle 
from time import sleep
turtle.shape("turtle")
degree=1
crug=360
turn=60
def circle(r):
	for i in range(crug):
		turtle.forward(degree)
		if r==0:
			turtle.left(degree)
		else:
			turtle.right(degree)
for i in range(1,3):
	for r in range(2):
		circle(r)
	turtle.left(turn)
