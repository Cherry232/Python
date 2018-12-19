print ("Hoi ik ben Kirsten en hier komt weer een nieuwe tekening met mijn geliefde turtle ik hoop dat jullie hem leuk vinden!")

import turtle
Jurjen = turtle.Turtle()
Jurjen.speed(50)
Jurjen.shape("turtle")
Jurjen.color("red")

Jurjen.penup()
Jurjen.forward(500)
Jurjen.pendown()

for i in range(5,106,3):
    Jurjen.forward(i*2)
    Jurjen.right(90)

import turtle
anna=turtle.Turtle()
anna.speed (50)
anna.shape("turtle")
anna.color("blue")

for i in range(5,106,3):
  anna.forward(i*2)
  anna.right(90)
  
import turtle
wouter=turtle.Turtle()
wouter.speed(50)
wouter.shape("turtle")
wouter.color("green")

wouter.penup()
wouter.backward(500)
wouter.pendown()

for i in range(5,106,3):
    wouter.forward(i*2)
    wouter.right(90)
  
