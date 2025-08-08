import turtle

t = turtle.Turtle()
s = turtle.Screen()
colors = ['orange', 'magenta', 'red', 'blue', 'yellow', 'green', 'cyan', 'purple', 'white']

s.bgcolor('black')
t.pensize(2)
t.speed(0)

for x in range(300):
    t.pencolor(colors[x % len(colors)])
    t.width(x // 100 + 1)
    t.forward(x)
    t.right(59)

t.hideturtle()
turtle.done()
