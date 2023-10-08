# CS 122 Fall 2023 Lab 2
# Author: Oliver Boorstein
# Partner:
# Description: Calculate the average amount of time in seconds light
# will take to reach the surface of the Earth and Jupiter

# Initialize variables
speed_light_seconds = 186282

# Define function to calculate light travel time for given distance
def avg_light_travel_seconds(miles):
    # return rounded miles / speed
    return round((miles / speed_light_seconds), 2)


# Define function to display results of calculation
def print_results(planetary_object, time_to_object):
    # print light travels to planet in x secs
    print(f"Light travels from the sun to {planetary_object} an average of {time_to_object} seconds.")

# Test
print_results("the Earth", str(avg_light_travel_seconds(93000000)))
print_results("Jupiter", str(avg_light_travel_seconds(484000000)))