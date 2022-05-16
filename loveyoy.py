import turtle
from turtle import *

wn = Screen()
wn.bgcolor("red")

t = turtle.Turtle()
t.pencolor("purple")
t.pensize(2)
t.speed(100)

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)


def heart():
    t.fillcolor("pink")
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()

def write(message,pos):
    x,y = pos
    t.penup()
    t.goto(x, y)
    t.color("red")
    style=("Stencil Std", 20, "bold")
    t.write(message, font=style)
write('J', (-14, 95))
write('I', (10, 95))
wn.mainloop()

    
