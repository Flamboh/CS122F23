"""
CS 122 Fall 2023 Project 6 Random
Author: Oliver Boorstein
Credit:
Description: Read lines of file with numbers and add up while skipping comments and display aeverage.
"""

from p6_shared import pad_left, pad_right
import os


lines_comments = 0
lines_not_comments = 0
nums_total = 0
average_num = 0
label_spacing = 10
num_spacing = 10

while True:
    file_name = input("Enter filename (blank to exit): ").strip()
    if file_name == "":
        break
    elif not os.path.exists(file_name):
        print(f"Invalid filename: {file_name}")
        # I knew there was something like continue that existed from previous coding experience and I found it at this link: https://www.tutorialspoint.com/python/python_loop_control.htm#:~:text=The%20continue%20statement%20in%20Python,both%20while%20and%20for%20loops.
        continue
    num_list = open(file_name)

    for line in num_list:
        if line[0] == '#':
            lines_comments += 1
        else:
            lines_not_comments += 1
            nums_total += int(line)

    num_list.close()

    average_num = round((nums_total / (lines_not_comments)), 2)

    print(f"{pad_right('Count:', label_spacing)}{pad_left(lines_not_comments, num_spacing)}")
    print(f"{pad_right('Comments:', label_spacing)}{pad_left(lines_comments, num_spacing)}")
    print(f"{pad_right('Total:', label_spacing)}{pad_left(nums_total, num_spacing)}")
    print(f"{pad_right('Average:', label_spacing)}{pad_left(average_num, num_spacing)}")
    
