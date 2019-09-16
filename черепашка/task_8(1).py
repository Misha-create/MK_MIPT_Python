import turtle

turtle.shape('turtle')

def spir(left, right, acc): 
    for i in range(acc):
        for j in range(4):
            turtle.forward(left+right*(i*4+j))
            turtle.left(90)

spir(5, 2, 10)
