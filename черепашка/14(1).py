import turtle as t
full=360
pi=180
t.shape("turtle")
def star(n):
    for i in range(n):
        t.forward(100)
        if n % 2 == 1:
            t.right(pi - pi / n)
        else:
            t.right(pi - full / n)


star(5)

