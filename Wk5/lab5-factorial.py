"""
CS 122 Fall 2023 Lab 5 Factorial
Author: Oliver Boorstein
Credit:
Description: Write a factorial function
"""

import math

def factorial(num):
    num = float(num)
    num = int(num)
    # if the number is invalid print an error and return none
    if num < 0:
        print("Error: Number must be >= 0")
        return None
    # if number == 0 output 1
    if num == 0:
        return 1
    # process factorial
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def test_factorial(num, show=False):
    errors = 0
    range_num = num + 1
    for i in range(range_num):
        a = factorial(i)
        b = math.factorial(i)
        if show:
            print(f"{i} : {a} {b}")
        if a != b:
            errors += 1
            print(f"{num} : {a} {b}")
    print(f"Errors ({num}): {errors}")
            

# test_factorial(5, True)

# Take input of number
num = input("Enter factorial number: ")

print(factorial(num))

