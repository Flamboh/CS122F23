"""
CS 122 Fall 2023 Lab 4 Calendar
Author: Oliver Boorstein
Credit:
Description: Creating calendar-related functions
"""

import calendar

# Declare Functions

def get_full_month(int):
    month = ""

    if int == 1:
        month = "January"
    
    elif int == 2:
        month = "February"
    
    elif int == 3:
        month = "March"
    
    elif int == 4:
        month = "April"
    
    elif int == 5:
        month = "May"
    
    elif int == 6:
        month = "June"
    
    elif int == 7:
        month = "July"
    
    elif int == 8:
        month = "August"
    
    elif int == 9:
        month = "September"
    
    elif int == 10:
        month = "October"
    
    elif int == 11:
        month = "November"
    
    elif int == 12:
        month = "December"

    else:
        print(f"Must be an integer between 1 and 12 ({int} is invalid)")
        month = ""
    
    return month

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    
    else: 
        return False

def test_get_full_month():
    for i in range(14):
        print(i, get_full_month(i))

def test_is_leap_year(start_year, end_year):
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            print(year)

def validate_is_leap_year(start_year, end_year):
    for year in range(start_year, end_year + 1):
        a = calendar.isleap(year)
        b = is_leap_year(year)
        if a != b:
            print("Mismatch")
        else:
            print("match")
        

# Test

test_get_full_month()

test_is_leap_year(1996, 2112)

validate_is_leap_year(1996, 2112)