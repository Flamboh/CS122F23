# CS 122 Fall 2023 Project 2 Cement
# Author: Oliver Boorstein
# Credit:
# Description: You volunteered to help pour two cement slabs for a friend
# Your friend asked you to calculate the amount of cement you would need

# References:
# https://todayshomeowner.com/lawn-garden/video/cubic-yard-calculator/
# https://www.concretenetwork.com/concrete/howmuch/calculator.htm
# https://stackoverflow.com/questions/70910711/cant-print-inch-and-feet-symbols-in-function For help with the print results f-string solution


import math

# Inititalize variables
total_inches_in_cubic_yard = round(math.pow(36, 3)) # 36 inches in a in 1 dimensional yard to the 3rd power for cubic

# Return cement amount in yards using cubic inches given thickness (t), width (w) and length (l) in inches
def calc_yards_cement(t, w, l):
    total_cubic_yards_in_slab = t * w * l
    yards_needed = total_cubic_yards_in_slab / total_inches_in_cubic_yard

    return round(yards_needed, 2)
    

# Output (print) results of calculating yards given thickness (t), width (w) and length (l) in inches
def print_results(t, w, l):
    print(f"A cement slab {t}\" thick, {w}\" wide and {l}\" long requires", calc_yards_cement(t, w, l), "cubic yards of cement")


# Use created functions to display results
print_results(4, 72, 120)
print_results(4, 120, 240)
