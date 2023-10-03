# CS 122 Fall 2023 Project 1 
# Author: Oliver Boorstein
# Credit:
# Description: Introduction to programming problem set uses Python numeric data types and 
# operations to solve a variety of small problems.

#
# Question 1
#

print("Question 1")
print("------------------------------------------")

# Calculate the number of watermelons given 70 children at 3 slices,
# 80 adults at 2 slices, 14 slices per watermelon, add 25% extra, rounding up.

import math


# Initialize variables with values
adults = 80
children = 70

slices_per_adult = 2
slices_per_child = 3
extra = 0.25

slices_per_watermelon = 14

# Calculate total number of watermelon slices and display number of slices
total_slices = (children * slices_per_child) + (adults * slices_per_adult)
print("Total slices:", total_slices)

# Add extra amount and display number of slices
total_slices = total_slices + (total_slices * extra)
print("Total slices (including extra):", total_slices)

# Calculate number of watermelons and display number of watermelons
watermelons = total_slices / slices_per_watermelon
print("Total watermelons:", watermelons)

# Round the number of watermelons up and display number of watermelons
watermelons = math.ceil(watermelons)
print("Total watermelons (rounded up):", watermelons)

#
# Question 2
#

print()
print("Question 2")
print("------------------------------------------")

# Calculate total number of trips given 50, 100, 200 or 500 daily steps, 14
# steps per floor, and down and back up the stairs as one trip. Re-use the
# step variable. Round the number of trips up to the nearest whole integer.
# Recommended variable names: steps_per_floor, target_steps, trips

import math


# Initialize variables
steps_per_floor = 14
floor = 4
target_steps = 0
trips = 0

# Calculate steps per trip. It is multiplied by 2 for down then back up
steps_per_trip = steps_per_floor * floor * 2

# Calculate trips for 50 steps and display number of trips
target_steps = 50

trips = target_steps / steps_per_trip
trips = math.ceil(trips)

print("Trips for", target_steps, "steps:", trips)

# Calculate trips for 100 steps and display number of trips
target_steps = 100

trips = target_steps / steps_per_trip
trips = math.ceil(trips)

print("Trips for", target_steps, "steps:", trips)

# Calculate trips for 200 steps and display number of trips
target_steps = 200

trips = target_steps / steps_per_trip
trips = math.ceil(trips)

print("Trips for", target_steps, "steps:", trips)

# Calculate trips for 500 steps and display number of trips
target_steps = 500

trips = target_steps / steps_per_trip
trips = math.ceil(trips)

print("Trips for", target_steps, "steps:", trips)

#
# Question 3
#

print()
print("Question 3")
print("------------------------------------------")

# Calculate total distance walked per week given a pivot radius of 200 feet,
# six pivots, two inspections per day, and working five days a week. Round
# all results to two decimal places. Use 3.14, or math.pi, for the circumference
# equation calculation.

import math


# Initialize variables
pi = math.pi
radius = 200
days_worked = 5
num_center_pivots = 6
times_inspected = 2
weekly_distance = 0
feet_per_mile = 5280

# Calculate center pivot system circumference in feet
cps_circumference = radius * 2 * pi

# Calculate and display weekly distance walked in feet
weekly_distance = cps_circumference * times_inspected * days_worked * num_center_pivots
print("Weekly distance (feet):", round(weekly_distance, 2))

# Calculate and display weekly distance walked in miles
weekly_distance = weekly_distance / feet_per_mile
print("Weekly distance (miles):", round(weekly_distance, 2))