import turtle

def draw_square(t, size):
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)


morla = turtle.Turtle()

# draw_square(morla, 100)

for i in range(1, 100):
    for j in range(1, 5):
        draw_square(morla, j * i)
    if i > 2:
        turtle.Terminator(morla)
