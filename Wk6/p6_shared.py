"""
CS 122 Fall 2023 Project 6 Shared
Author: Oliver Boorstein
Credit:
Description: Create three functions for padding a string
"""

def pad_string(data, size, direction = 'left', char = ' '):
    data = str(data)
    padded_data = ""
    if len(data) > size:
        padded_data = data
    elif direction == 'left':
        padded_data = ((char * (size - len(data))) + data)
    elif direction == 'right':
        padded_data = data + (char * (size - len(data)))
    return padded_data

def pad_left(data, size, char = ' '):
    return pad_string(data, size, 'left', char)

def pad_right(data, size, char = ' '):
    return pad_string(data, size, 'right', char)
