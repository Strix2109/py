import turtle


turtle.setup(1440,900)
turtle.bgcolor('black')

# Setup
t = turtle.Turtle()
t.penup()
t.goto(-40,-50)
t.pendown()

# Yellow Square
t.color('yellow')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

# Orange Parallelogram 
t.color('orange')
t.begin_fill()
t.left(135)
t.forward(60)
t.right(45)
t.forward(100)
t.left(45)
t.backward(60)
t.end_fill()

# Red Parallelogram
t.color('red')
t.begin_fill()
t.penup()
t.forward(60)
t.right(45)
t.right(90)
t.pendown()
t.forward(100)
t.right(45)
t.forward(60)
t.end_fill()
t.penup()
t.color('black')
t.forward(100)

turtle.done()
