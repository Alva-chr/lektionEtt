import turtle
import random

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def make_turtle(x, y):
    t = turtle.Turtle()
    t.shape('turtle')
    jump(t, x, y)
    return t

def move_random(t):
    vinkel = random.randint(-45,45)
    strackan = random.randint(0,25)

    if t.xcor() < 250 and t.xcor() > -250 and t.ycor() < 250 and t.ycor() > -250:
        t.left(vinkel)
    
    else:
       t.setheading(t.towards(0,0)) 

    t.forward(strackan)



def rectangle(x, y, width, height, color):
    t = make_turtle(x, y)
    t.hideturtle()
    t.speed(0)
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

rectangle(-250,-250,500,500,'lightblue')

turtleOne = make_turtle(random.randint(-250, 250), random.randint(-250,250))
turtleOne.color('blue')

turtleTwo = make_turtle(random.randint(-250, 250), random.randint(-250,250))
turtleTwo.color('red')

turtleClose = 0

for i in range(500):
    move_random(turtleOne)
    move_random(turtleTwo)

    if turtleOne.distance(turtleTwo) < 50:
        turtleOne.write('close')
        turtleClose = turtleClose + 1

print(turtleClose)

turtle.done()



