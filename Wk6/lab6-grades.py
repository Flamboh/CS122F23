"""
CS 122 Fall 2023 Lab 6 Grades
Author: Oliver Boorstein
Credit:
Description: Write a program to find an average grade
"""

# Initialize variables
grades_count = 0
grades_total = 0
grades_average = 0
grades_low = 0
grades_high = 0

while True:
    grade = input("Enter score: ")
    if grade == "":
        break
    grade = int(grade)
    grades_total += grade
    grades_count += 1
    grades_average = grades_total / grades_count
    if grades_count == 1:
        grades_low = grade
        grades_high = grade
    else:
        if grades_low > grade:
            grades_low = grade
        if grades_high < grade:
            grades_high = grade

print(f"*** Results ***\nCount: {grades_count}\nAverage: {grades_average}\nLow score: {grades_low}\nHigh score: {grades_high}")
