from turtle import Turtle
t = Turtle()

def drawCircle(t, radius):
    length = (2.0 * 3.14 * radius) / 120.0
    for count in range(120):
        t.forward(length)
        t.right(3)

drawCircle(t, 100)


