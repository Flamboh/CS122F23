# Import Turtle graphics module and create a turtle for drawing
import turtle
t = turtle.Turtle()

def draw_circle(t, radius, x, y):
    """
    Draw a circle of length radius using Turtle T at given (x, y) position
    """
    move(t, x, y - radius)
    t.circle(radius)

def move(t, x, y):
    """
    Move turtle to given (x, y) position
    """
    t.pu()
    t.goto(x, y)
    t.pd()

def draw_concentric_circles(t, num_circles, start_size, circle_gap, x, y):
    """
    Draw given number of circles with a specifc starting size and gap between each circle at given (x, y) position
    """
    for i in range(num_circles):
        draw_circle(t, start_size, x, y)
        start_size += circle_gap
# Test
draw_concentric_circles(t, 3, 50, 25, 0, 0)
