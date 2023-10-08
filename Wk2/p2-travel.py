# CS 122 Fall 2023 Project 2 Travel
# Author: Oliver Boorstein
# Credit:
# Description: While traveling home for the holiday, you 
# wondered how much time you'd save if you drove faster

# References:
# https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php


# Calculate travel time in minutes given the distance in miles and the speed in mph
def calc_travel_time(distance, speed):
    travel_time = distance / speed

    travel_time *= 60

    return travel_time

# print(calc_travel_time(10, 25))

# Output the travel time hours, minutes and seconds given distance and speed
def print_travel_time(distance, speed):
    travel_time = calc_travel_time(distance, speed)
    
    # Convert from mins.decimal to hrs, mins, secs
    hours = travel_time / 60
    minutes = travel_time % 60
    seconds = 60 * (minutes % 1)

    print(f"To travel {distance} miles at {speed} MPH will take {int(hours)} hr, {int(minutes)} min and {round(seconds)} sec")

# Test
print_travel_time(90, 55)
print_travel_time(90, 70)
print_travel_time(10, 25)
print_travel_time(10, 35)
