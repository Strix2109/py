import turtle
wn=turtle.Screen()
turtle.bgcolor('black')
turtle.shape('turtle')
tr=turtle.Turtle()
ts=turtle.Turtle()
tt=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
move=1
###############################
t5.speed("fast")
for i in range(6):
    for i in range(4):
          t5.pu()
          t5.goto(0,0)
          t5.pd()
          t5.color('light green')
          t5.pensize(3)
          t5.circle(100,steps=6)
          t5.right(100)
