from turtle import Turtle
t = Turtle()

def drawFractalLine(t, length, angle, level):
    if level == 0:
        t.forward(length)
    else:
        drawFractalLine(t, length / 3, angle, level - 1)
        t.left(60)
        drawFractalLine(t, length / 3, angle, level - 1)
        t.right(120)
        drawFractalLine(t, length / 3, angle, level - 1)
        t.left(60)
        drawFractalLine(t, length / 3, angle, level - 1)

def drawKochSnowflake(t, length, level):
    for angle in (0, -120, 120):
        drawFractalLine(t, length, angle, level)
        t.right(120)

t.speed(0)
drawKochSnowflake(t, 200, 4)
