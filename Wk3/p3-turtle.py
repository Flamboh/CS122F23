"""
CS 122 Fall 2023 Project 3 Turtle
Author: Oliver Boorstein
Credit:
Description: Create a void function to draw a line using Python's Turtle graphics
"""

import turtle

def draw_line(t, x, y, angle, length):
    """
    Draw a line using Turtle graphics

    Draw a line at a specifc location with a specific length and angle. Start and end with pen up
    
    Args:
        t (Turtle): Drawing turtle
        x (int): starting x value of Turtle
        y (int): starting y value of Turtle
        angle (int): starting angle of Turtle
        length (int): total length of line
        
    Returns:
        None (void)
    """
    t.pu()
    t.setx(x)
    t.sety(y)
    t.seth(angle)
    t.pd()
    t.fd(length)
    t.pu()

def draw_radial_lines(t, x, y, length, num_lines):
    """
    Draw radial lines using Turtle graphics
    
    Draw radial lines at a specific location with a specific length and angle. Start and end with pen up
    
    Args:
        t (Turtle): Drawing turtle
        x (int): x value for origin of radial
        y (int): y value for origin of radial
        length (int): length of the lines
        num_lines (int): number of lines in radial
        
    Returns:
        None (void)
    """

    for i in range(num_lines):
        angle = i * 360 / num_lines
        draw_line(t, x, y, angle, length)

def draw_radials_in_quadrants(t, length, num_lines):
    """
    Draw radial lines with one in each quadrant

    Separated by twice the length of lines

    Args:
        t (Turtle): Drawing turtle
        length (int): length of lines
        num_lines (int): number of lines drawn in a radial
    
    Returns:
        None (void)
    """
    # quad_1_x = (length * 2)
    # quad_1_y = (length * 2)
    # quad_2_x = -(length * 2)
    # quad_2_y = (length * 2)
    # quad_3_x = -(length * 2)
    # quad_3_y = -(length * 2)
    # quad_4_x = (length * 2)
    # quad_4_y = -(length * 2)
    # draw_radial_lines(t, quad_1_x, quad_1_y, length, num_lines)
    # draw_radial_lines(t, quad_2_x, quad_2_y, length, num_lines)
    # draw_radial_lines(t, quad_3_x, quad_3_y, length, num_lines)
    # draw_radial_lines(t, quad_4_x, quad_4_y, length, num_lines)

    draw_radial_lines(t, length * 2, length * 2, length, num_lines)
    draw_radial_lines(t, -length * 2, length * 2, length, num_lines)
    draw_radial_lines(t, -length * 2, -length * 2, length, num_lines)
    draw_radial_lines(t, length * 2, -length * 2, length, num_lines)


pen = turtle.Turtle()
# Test

# draw_line(pen, 50, 50, 0, 50)
# draw_line(pen, -50, -50, 135, 75)
# draw_line(pen, 100, -100, 270, 100)

# draw_radial_lines(pen, -50, -50, 10, 4)
# draw_radial_lines(pen, -50, 50, 20, 8)
# draw_radial_lines(pen, 50, -50, 40, 16)
# draw_radial_lines(pen, 50, 50, 80, 20)


draw_radials_in_quadrants(pen, 25, 3)
draw_radials_in_quadrants(pen, 50, 9)