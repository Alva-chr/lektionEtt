import turtle

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    return t

def rectangle(x, y, width, height, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.fillcolor(color)

    t.penup()
    t.goto(x,y)
    t.pendown


    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()
    
def tricolore(x,y,h):
    w = h/2
    rectangle(x,y,w,h,'blue')
    rectangle(x+w,y,w,h,'white')
    rectangle(x+2*w,y,w,h, 'red')

def pentagram(x,y,side,color = 'green'):
    t = make_turtle(x,y)
    t.speed(0)
    t.hideturtle()
    t.setheading(270 + 36/2)
    t.fillcolor(color)

    t.begin_fill()
    for i in range(5):
        t.forward(side)
        t.right(180-36)
    t.end_fill()

#start värden för rektangel
h = 200
w=h/2

#start koordnitar för rektangel
rectStartX = -1.5*w
rectStartY = -h/2

#start koordniater för pentagram

pentaStartX = rectStartX -w/2
pentaStartY = h + w

tricolore(rectStartX,rectStartY,h)

for i in range(0,5):
    pentagram(pentaStartX + (i*w), pentaStartY, w)
    pentagram(pentaStartX + (i*w), -pentaStartY + h - w, w)



turtle.done()