"""
CS 122 Fall 2023 Project 3 Reverse
Author: Oliver Boorstein
Credit:
Description: Write a fruitful function reverse() that accepts a string
and will return the string in reverse order
"""

# Initialize Variables

original_string = "When in the course of human events"

# Reverse string 
    # loop through string
    # Concatenate first character to end of reversed_string
    #
    # Return reversed_string

def reverse(str):
    """
    Reverses given string

    Loops through str to concatenate it to reversed_string

    Args:
        str (str): string inputted on function call

    Returns:
        the variable reversed_string
    """
    reversed_string = ""
    for i in str:
        reversed_string = i + reversed_string
    return(reversed_string)

# Print

print("Original:", original_string)
print("Reversed:", reverse(original_string))