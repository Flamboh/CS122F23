"""
CS 122 Fall 2023 Project 8 Group Manager
Author: Oliver Boorstein
Credit:
Description: Manage groups
"""

def group_help():
    print("?: List commands\nC: Create a new group\nA: Add data to a group\nG: List groups\nL: List data for a group\nX: Exit\n")

def create_group(d):
    print("** Create new group **\n")
    while True:
        group_name = input("Enter group name (empty to cancel): ")
        if group_name == "":
            print()
            break
        elif group_name in d:
            print("Group already exists\n")
        else:
            fields = []
            while True:
                field_to_add = input("Enter field name (empty to stop): ")
                if field_to_add == "":
                    print()
                    break
                else:
                    fields.append(field_to_add)
            d[group_name] = {
                '__fields__': fields,
                '__data__': [

                ]
            }

        

def list_groups(d):
    print("** List of groups **")
    for group in d:
        field_list = ', '.join(d[group]['__fields__'])
        print(f"{group} : {len(d[group]['__fields__'])} properties ({field_list})")
    print()

def add_group_data(d):
    print("** Add group data **")
    list_groups(d)

    while True:
        group = input("Enter group (empty to cancel): ")
        if group == '':
            break
        elif group not in d:
            print("Group does not exist")
        else:
            item = {}
            for field_index in range(len(d[group]['__fields__'])):
                item[d[group]['__fields__'][field_index]] = input(f"Enter {d[group]['__fields__'][field_index]}: ")    
            d[group]['__data__'].append(item)
            print()       
    print()

def list_group_data(d):
    print("** List group data **")
    list_groups(d)

    while True:
        group = input("Enter group name (empty to cancel): ")
        if group == '':
            break
        elif group not in d:
            print("Group does not exist")
        else:
            item_num = 0
            for item in d[group]['__data__']:
                t = []
                for key in item:
                    t.append(f"{key} = {item[key]}")
                item_list = ', '.join(t)    
                print(f"{item_num} {item_list}")
                item_num += 1
            print()    
    print()


print(">> Welcome to Group Manager <<")
print("This program creates groups with dynamic properties\n")

d = {}
while True:
    # Get command
    command = input("Command (empty or X to quit, ? for help): ").strip().upper()
    # Check if command is to exit
    if command == '' or command == 'X':
        break
    elif command == '?':
        group_help()
    elif command == 'C':
        create_group(d)
    elif command == 'G':
        list_groups(d)
    elif command == 'A':
        add_group_data(d)
    elif command == 'L':
        list_group_data(d)
