# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 14:27:19 2024

q:quit
up,down: forward, backward movestep
left,right: turn left or right anglestep

u: penup
d: pendown
c: color choose
a: anglestep setup
s: movestep setup

mouse left click: person
mouse right click: GZ (George Zeng )

@author: zeng_
"""

import turtle as t
from tkinter import colorchooser

time="day"

screen = t.Screen()

screen.setup(1.0, 1.0)

t.speed(0)

if time == "morning":
   screen.bgcolor("skyblue")
elif time == "day":
   screen.bgcolor("#d2e7ff")
elif time == "afternoon":
   screen.bgcolor("#1ca2ef")
elif time == "evening":
   screen.bgcolor("#ffc84d")
elif time == "night":
   screen.bgcolor("#0c1445")
else:
    screen.bgcolor("skyblueday")
    
t.pendown()
t.pencolor("red")
t.shape("turtle")
print("ok1")
moveStep=20
angleStep=30

def turtleQuit():
    t.bye()
    
def turtleUp():
    t.penup()
    
def turtleDown():
    t.pendown()

def turtlefd():
    t.forward(moveStep)
    
def turtlebk():
    t.backward(moveStep)
    
def turtleLeft():
    t.left(angleStep)
    
def turtleRight():
    t.right(angleStep)
    
def turtleColor():
    acolor=colorchooser.askcolor()
    t.pencolor(acolor[1])
    
def turtleStep():
    global moveStep
    step=t.numinput("step","Move Step".moveStep,1,100)
    moveStep=step
    screen.listen()
    
def turtleAngleStep():
    global angleStep
    step=t.numinput("angle step","Move angle  Step".anglStep,1,100)
    angleStep=step
    screen.listen()
    

screen.onkey(turtlefd, "Up")
screen.onkey(turtlebk, "Down")
screen.onkey(turtleLeft, "Left")
screen.onkey(turtleRight, "Right")

screen.onkey(turtleQuit, "q")
screen.onkey(turtleUp, "u")
screen.onkey(turtleDown, "d")
screen.onkey(turtleAngleStep, "a")
screen.onkey(turtleStep, "s")
screen.onkey(turtleColor, "c")
#screen.onkey(turtle, "")

def initials():
    t.pensize(3)
    if time == "night":
        t.color("#f3ebba")
    i=t
    i.setheading(180)
    i.circle(30, 180)
    i.forward(10)
    i.left(90)
    i.forward(20)
    i.left(90)
    i.forward(10)
    i.backward(20)
    i.left(90)
    i.penup()
    i.forward(20)
    i.left(90)
    i.forward(15)
    i.pendown()
    i.forward(20)
    i.backward(30)
    i.left(65)
    i.forward(65)
    i.right(245)
    i.forward(30)
def person(x,y):

   t.penup()
   t.setpos(x, y)
   t.setheading(225)
   t.pendown()
   t.forward(35)
   t.backward(35)
   t.left(90)
   t.forward(35)
   t.backward(35)
   t.left(135)
   t.forward(25)
   t.right(90)
   t.forward(25)
   t.backward(50)
   t.forward(25)
   t.left(90)
   t.forward(25)
   t.right(90)
   t.circle(20)
   t.left(90)
   t.penup()
   t.forward(20)
   t.right(90)
   t.forward(7)
   t.pendown()
   t.circle(5)
   t.penup()
   t.backward(14)
   t.pendown()
   t.circle(5)
   t.penup()
   t.right(90)
   t.forward(7)
   t.pendown()
   t.circle(7, 180)    
    
def left_click(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.speed(0)
    initials()
    
screen.onclick(person, 1)
screen.onclick(left_click,3)
#screen.onclick(left_click, 0)

screen.listen()
t.mainloop()