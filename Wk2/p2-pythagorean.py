# CS 122 Fall 2023 Project 2 Pythagorean
# Author: Oliver Boorstein
# Credit:
# Description: Calculate the missing side of a triangle
# using the Pythagorean Theorem

# References:
# https://www.rapidtables.com/calc/math/pythagorean-calculator.html
# https://docs.python.org/3/library/math.html
# https://www.nctm.org/classroomresources/

import math

# Calculate missing side C
def calc_side_c(a, b):
    c = math.sqrt(pow(a, 2) + pow(b, 2))

    return round(c, 2)



# Calculate missng side A or B
def calc_side_ab(ab, c):
    missing_leg = math.sqrt(pow(c, 2) - pow(ab, 2))

    return round(missing_leg, 2)

# Test functions and display results
print("c =", calc_side_c(5, 10))

print("a/b =", calc_side_ab(4, 8))

