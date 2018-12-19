import turtle

t = turtle.Turtle()
t.shape("turtle")

t.speed(500)

def vorm(aantalhoeken):
    for i in range (aantalhoeken):
        t.forward(50)
        t.right(360/aantalhoeken)
        
vorm(3)
vorm(4)
vorm(5)
vorm(6)
vorm(7)
vorm(8)
vorm(9)
t.penup()
t.forward(999999)