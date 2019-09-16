import turtle 
import math
from time import sleep
turtle.shape("turtle")
r=180
def nug(n,x):
	vn=r*(n-2)/n
	ug=r-vn
	turtle.right(vn/2)
	for i in range(n):
		turtle.forward(x)
		turtle.left(ug)
	turtle.left(vn/2)
def a(R,n):
	return 2*R*math.sin(math.pi/n) 
R=10
turtle.left(r)
somepoint=30
for i in range(3,13): 
	nug(i,a(R,i))
	turtle.penup()
	turtle.backward(somepoint)
	R+=somepoint
	turtle.pendown()

