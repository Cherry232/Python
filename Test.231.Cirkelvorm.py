import turtle

t = turtle.Turtle()
t.speed(999999)

t.shape("turtle")

def cirkel():
    for i in range(205):
        t.forward(5)
        t.right(5)
        
        
def vorm(aantalhoeken):
    for i in range(aantalhoeken):
        t.forward(100)
        t.right(360/aantalhoeken)

for i in range(10):
    cirkel()
    t.penup()
    t.left(40)
    t.forward(40)
    t.pendown()
    vorm(4)
    t.penup()
    t.left(40)
    t.forward(40)
    t.pendown()

    
t.penup()
t.forward(500)
    
