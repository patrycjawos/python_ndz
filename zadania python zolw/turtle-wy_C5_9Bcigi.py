from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)

for krok in range(16):
    write(krok)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ala = Turtle()
ala.color('red')
ala.shape('turtle')
ala.penup()
ala.goto(-160,100)
ala.pendown()

alek = Turtle()
alek.color('blue')
alek.shape('turtle')
alek.penup()
alek.goto(-160,70)
alek.pendown()

for tura in range(100):
    ala.forward(randint(1,5))
    alek.forward(randint(1,5))