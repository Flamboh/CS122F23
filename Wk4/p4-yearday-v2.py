"""
CS 122 Fall 2023 Project 4 Yearday-v4
Author: Oliver Boorstein
Credit:
Description: Write a program to calculate year and day given user input 
but more optimized this time
"""

def is_leap_year(year):
    """
    Check if a given year is a leap year
    
    Args:
        year (int): """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    
    else: 
        return False
    
def valid_year(year):
    if year <= 0:
        print("Year must be > 0")
        return False
    else:
        return True
    
def valid_day_of_year(year, day_of_year):
    if day_of_year <= 0:
        print("Day of year must be > 0")
        return False
    elif day_of_year > get_days_in_year(year):
        print(f"Day of year must be <= {get_days_in_year(year)}")
        return False
    else:
        return True
    
def input_year():
    year = int(input("Enter year: "))
    if not valid_year(year):
        return 0
    else:
        return year

def input_day_of_year(year):
    day_of_year = int(input("Enter day of year: "))
    if valid_year(year) and valid_day_of_year(year, day_of_year):
        return day_of_year
    else:
        return 0

def get_days_in_year(year):
    if not valid_year(year):
        return 0
    elif is_leap_year(year):
        return 366
    else:
        return 365

def valid_month(month):
    if month <= 0:
        print("Month must be > 0")
        return False
    elif month > 12:
        print("Month must be <= 12")
        return False
    else:
        return True

def translate_month(month):
    if not valid_month(month):
        return ""
    elif month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"

def get_days_in_month(year, month):
    if not valid_month(month) or not valid_year(year):
        return 0
    elif month == 1:
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31

def valid_day(year, month, day):
    if valid_year(year) and valid_month(month) and valid_day_of_year(year, day):
        return True
    else:
        return False
    
def get_date_string(year, month, day):
    if not valid_day(year, month, day):
        return ""
    else:
        return f"{translate_month(month)} {day}, {year}"


def start():


        
    days_so_far = 0
    month = ""
    day_in_month = 0

    # step1: prompt for year
    year = int(input_year())

    if not year:
        # I know quit from previous coding experience so I thought to use that as it is easier than the other options
        quit()

    # step3: prompt for a day of the year
    day_of_year = int(input_day_of_year(year))

    if not day_of_year:
        quit()
    
    # step4: loop through months
    for month in range(1, 13):
        # step5: check each month
        if month == 1:
            days_so_far += get_days_in_month(year, month)
            # step6: check if the day of year is less than the days we've checked before if it is we are in correct month
            if day_of_year <= days_so_far:
                # step7: calculate which day in the month we are
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 2:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 3:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 4:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 5:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 6:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 7:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 8:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 9:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 10:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 11:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

        elif month == 12:
            days_so_far += get_days_in_month(year, month)
            if day_of_year <= days_so_far:
                day_in_month = day_of_year - (days_so_far - get_days_in_month(year, month)) 
                break

    print(get_date_string(year, month, day_in_month))




start()