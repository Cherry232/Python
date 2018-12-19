import turtle

t = turtle.Turtle()
t.speed(999999)

t.shape("turtle")

def cirkel():
    for i in range(205):
        t.forward(5)
        t.right(5)

for i in range(72):
    cirkel()
    t.penup()
    t.left(40)
    t.forward(40)
    t.pendown()
    
t.penup()
t.forward(500)
    
