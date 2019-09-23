import turtle 
import math
tpi=360
point=1
turtle.shape("turtle")
def circle(n,rl):
    for i in range(math.ceil(tpi*(1+0.1*n))):
        turtle.forward(1)
        if rl:
            turtle.left(1/(1+0.1*n))
        else:
            turtle.right(1/(1+0.1*n))
allcircle=21
ppi=90
turtle.left(ppi)
for i in range(1,allcircle):
    for j in range(2):
        circle(i,j)
    
    
