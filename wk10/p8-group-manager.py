"""
CS 122 Fall 2023 Project 8 Group Manager
Author: Oliver Boorstein
Credit:
Description: Manage groups
"""

def group_help():
    print("?: List commands\nC: Create a new group\nA: Add data to a group\nG: List groups\nL: List data for a group\nX: Exit")

def create_group(d):
    pass

def list_groups(d):
    pass

def add_group_data(d):
    pass

def list_group_data(d):
    pass

while True:
    d = {}
    # Get command
    command = input("Command (empty or X to quit, ? for help): ").strip().upper()
    # Check if command is to exit
    if command == '' or command == 'X':
        break
    elif command == '?':
        group_help()
    elif command == 'C':
        create_group(d)

