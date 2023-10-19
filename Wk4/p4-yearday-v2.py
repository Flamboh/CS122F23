"""
CS 122 Fall 2023 Project 4 Yearday-v4
Author: Oliver Boorstein
Credit:
Description: Write a program to calculate year and day given user input 
but more optimized this time
"""

def is_leap_year(year):
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
    elif is_leap_year(year) and day_of_year > 366:
        print("Day of year must be <= 366")
        return False

    elif day_of_year > 365:
        print("Day of year must be <= 365")
        return False

    else:
        return True
    


def start():


        
    days_feb = 28
    days_so_far = 0
    month = ""
    day_in_month = 0

    # step1: prompt for year
    year = int(input("Please enter a year: "))
    valid_year(year)
    # step2: check if year is a leap year if yes increase days in february by 1

    if is_leap_year(year):
        days_feb += 1

    # step3: prompt for a day of the year
    day_of_year = int(input("Please enter a day: "))
    valid_day_of_year(year, day_of_year)

    # step4: loop through months
    for i in range(12):
        # step5: check each month
        if i == 0:
            days_current_month = 31
            days_so_far += days_current_month
            # step6: check if the day of year is less than the days we've checked before if it is we are in correct month
            if day_of_year <= days_so_far:
                month = "January"
                # step7: calculate which day in the month we are
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 1:
            days_current_month = days_feb
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "February"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 2:
            days_current_month = 31
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "March"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 3:
            days_current_month = 30
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "April"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 4:
            days_current_month = 31
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "May"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 5:
            days_current_month = 30
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "June"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 6:
            days_current_month = 31
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "July"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 7:
            days_current_month = 31
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "August"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 8:
            days_current_month = 30
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "September"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 9:
            days_current_month = 31
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "October"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 10:
            days_current_month = 30
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "November"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break

        elif i == 11:
            days_current_month = 31
            days_so_far += days_current_month
            if day_of_year <= days_so_far:
                month = "December"
                day_in_month = day_of_year - (days_so_far - days_current_month) 
                break


    print(f"{month} {day_in_month}, {year}")




# start()