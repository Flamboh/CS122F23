"""
CS 122 Fall 2023 Lab 10 Tuples
Author: Oliver Boorstein
Credit:
Description: Work with tuples
"""

import os

def number_stats(*args):

    # Initialize variables
    count = 0
    min_value = 0
    max_value = 0
    mean_value = 0
    median_value = 0

    # Calculate count
    count = len(args)
    
    # Calculate minimum value
    min_value = min(args)

    # Calculate maximum value
    max_value = max(args)

    # Calculate mean value
    mean_value = sum(args) / count

    # Calculate median value
    middle_index = count // 2
    if count % 2 == 0:
        median_value = (sorted(args)[middle_index] + sorted(args)[middle_index - 1 ]) /2
    else:
        median_value = sorted(args)[middle_index]
    
    return count, min_value, max_value, mean_value, median_value


while True:
    file_name = input("Enter filename (blank to exit): ").strip()
    if file_name == "":
        break
    elif not os.path.exists(file_name):
        print(f"Invalid filename: {file_name}")
        # I knew there was something like continue that existed from previous coding experience and I found it at this link: https://www.tutorialspoint.com/python/python_loop_control.htm#:~:text=The%20continue%20statement%20in%20Python,both%20while%20and%20for%20loops.
        continue
    data = open(file_name)
    
    d =  ()
    for line in data:
        d = d + (int(line.strip()),)


    count, min_val, max_val, mean_val, median_val = number_stats(*d)
    print(f"Count: {count}")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
    print(f"Mean: {mean_val}")
    print(f"Median: {median_val}")
