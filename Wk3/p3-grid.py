"""
CS 122 Fall 2023 Project 3 Grid
Author: Oliver Boorstein
Credit:
Description: Write a void function draw_grid() that accepts 
a single integer, and will print a grid of numbers
"""

def draw_grid(int):
    """
    Print a grid of integers 
    
    Counting up left to right on each row 
    Int x int size where int is the inputed number

    Args:
        int (int): inputed number
    
    Returns:
        None (void)
    """
    for i in range(int):

        for j in range (int):
            print(j + 1, end=' ')

        print()

draw_grid(3)
draw_grid(6)
draw_grid(10)