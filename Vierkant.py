import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(999999)
def vorm(aantalhoeken):
    for i in range(aantalhoeken):
        t.forward(100)
        t.right(360/aantalhoeken)

for i in range(2000):
    vorm(4)
    t.penup()
    t.left(40.23)
    t.forward(39.83)
    t.pendown()
        
t.penup()
t.forward(999999)

