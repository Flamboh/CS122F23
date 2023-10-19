"""
CS 122 Fall 2023 Project 4 Yearday-v1
Author: Oliver Boorstein
Credit:
Description: Write a program to calculate year and day given user input
"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    
    else: 
        return False
    
days_feb = 28
day_count = 365
days_so_far = 0
month = ""
day_in_month = 0

# step1: prompt for year
year = int(input("Please enter a year: "))
if year <= 0:
    print("Year must be > 0")
    quit()

# step2: check if year is a leap year if is increase day count and days in february by 1

if is_leap_year(year):
    day_count += 1
    days_feb += 1

# step3: prompt for a day of the year
day_of_year = int(input("Please enter a day: "))
if day_of_year <= 0 or day_of_year > day_count:
    print(f"Day must be between 1 and {day_count} for this year")
    quit()

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


# if is_leap_year(year) and day > 366:
#     print("Day must be between 1 and 366 for this year")

# elif is_leap_year(year) == False:
#     if day <= 0 or day > 365:
#         print("Day must be between 1 and 365 for this year")
#     else:
#         print("valid day")
# else:
#     print("valid day")

# # step4: find month of year
# month = ""
# days_so_far = 0
# day_of_month = 0
# days_in_current_month = 0

# for i in range(days_so_far, )

# for i in range(12):
#     if i == 0:
#         days_in_current_month = 31
#         days_so_far += days_in_current_month
#         if days_so_far >= day:
#             month = "January"
#             day_of_month = (days_so_far - days_in_current_month) + day
#             break

#     if i == 1:
#         days_in_current_month = days_feb
#         days_so_far += days_in_current_month
#         if days_so_far >= day:
#             month = "February"
#             day_of_month = (days_so_far - days_in_current_month) + day
#             break

#     if i == 2:
#         days_in_current_month = 31
#         days_so_far += days_in_current_month
#         if days_so_far >= day:
#             month = "March"
#             day_of_month = (days_so_far - days_in_current_month) + day
#             break

#     if i == 3:
#         days_in_current_month = 30
#         days_so_far += days_in_current_month
#         if days_so_far >= day:
#             month = "April"
#             day_of_month = (days_so_far - days_in_current_month) + day
#             break

#     if i == 4:
#         days_in_current_month = 30
#         days_so_far += days_in_current_month
#         if days_so_far >= day:
#             month = "May"
#             break

#     if i == 5:
#         days_so_far += days_jun
#         if days_so_far >= day:
#             month = "June"
#             break

#     if i == 6:
#         days_so_far += days_jul
#         if days_so_far >= day:
#             month = "July"
#             break

#     if i == 7:
#         days_so_far += days_aug
#         if days_so_far >= day:
#             month = "August"
#             break

#     if i == 8:
#         days_so_far += days_sep
#         if days_so_far >= day:
#             month = "September"
#             break

#     if i == 9:
#         days_so_far += days_oct
#         if days_so_far >= day:
#             month = "October"
#             break

#     if i == 10:
#         days_so_far += days_nov
#         if days_so_far >= day:
#             month = "November"
#             break

#     if i == 11:
#         days_so_far += days_dec
#         if days_so_far >= day:
#             month = "December"
#             break

# print(month)
# print(days_so_far, day, day_of_month)

# # step5: display month

# # step6: find day of year

# # step7: display day of year