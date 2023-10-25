import turtle


t = turtle.Turtle()

t.pensize(3)

t.fillcolor('red')

t.begin_fill()

t.lt(90)
t.circle(100,180)
t.lt(30)
t.fd(400)
t.lt(120)
t.fd(400)
t.lt(30)
t.circle(100,180)

t.end_fill()

t.pu()

t.setpos(-80, -50) 

t.color('pink')

t.write("Happy Birthday Addy!", font=("Verdana", 12, "bold"))

t.pu()

t.setpos(1000,1000)

turtle.Screen().exitonclick()