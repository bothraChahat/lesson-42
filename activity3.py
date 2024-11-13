import turtle
t = turtle.Turtle()
s = turtle.Screen()
color = ['red','purple','blue','green', 'orange', 'yellow']

s.bgcolor('black')
t.speed('fastest')
t.hideturtle()
while True:
    for x in range(200):
        t.pencolor(color[x%len(color)])
        t.forward(x)
        t.left(60)
    t.right(239)
    for x in range(200):
        t.pencolor('black')
        t.width(x/100 + 7)
        t.forward(x)
        t.right(59)

turtle.done()
