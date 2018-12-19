import turtle

t = turtle.Turtle()

t.shape("turtle")
t.color("red")

def maakvierkant():
  for i in range(4):
    t.right(90)
    t.forward(100)
    
for i in range(6):
  maakvierkant()
  t.right(60)