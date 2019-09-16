import turtle

turtle.shape('turtle')
n=1000
length = 1
radius = 1
x =0.0
k=5.0
a=3.0
for i in range(n):
	radius = k*3.14/180*a
	a+=3
	x = 2*3.14*radius/length
	turtle.forward(length)
	turtle.left(360/x)
