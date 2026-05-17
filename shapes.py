import turtle


screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(500, 400)
turtle.title("Polygons with Turtle")

t = turtle.Turtle()
t.speed(3)


t.color("red")
for i in range(3):
    t.forward(100)
    t.left(120)


t.penup()
t.goto(-150, -50)
t.pendown()

t.color("blue")
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.penup()
t.goto(150, -50)
t.pendown()

t.color("green")
for i in range(6):
    t.forward(70)
    t.left(60)

turtle.done()
