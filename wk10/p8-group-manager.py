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
        # Prompt for group name
        group_name = input("Enter group name (empty to cancel): ")
        # End loop if group name blank
        if group_name == "":
            print()
            break
        # Reprompt if group already exists
        elif group_name in d:
            print("Group already exists\n")
        else:
            # Blank list of fields to add to later
            fields = []
            while True:
                # The next field to add
                field_to_add = input("Enter field name (empty to stop): ")
                # Fields are done if blank
                if field_to_add == "":
                    print()
                    break
                else:
                    # Put next field at the end of the fields list so far
                    fields.append(field_to_add)
            # A group will have a name and will be a dictionary containing 2 keys: _fields_ and _data_
            # _fields_ will correspond to a list of fields
            # _data_ will correspond to a blank list for now, later that list will containd dictionaries
            # of items of that group type 
            d[group_name] = {
                '_fields_': fields,
                '_data_': [

                ]
            }

        

def list_groups(d):
    print("** List of groups **")
    # Loop through each group that exists
    for group in d:
        # The list of all the fields in the given group
        field_list = ', '.join(d[group]['_fields_'])
        # Display the group name, the number of fields, and the names of the fields
        print(f"{group} : {len(d[group]['_fields_'])} properties ({field_list})")
    print()

def add_group_data(d):
    print("** Add group data **")
    list_groups(d)

    while True:
        # Get group to add data to
        group = input("Enter group (empty to cancel): ")
        # End loop if group blank
        if group == '':
            break
        # If group does not exist reprompt
        elif group not in d:
            print("Group does not exist")
        else:
            # We are going to end up adding one item which contains a dictionary with the fields of the group as keys
            # and with our inputs as the values for each key
            item = {}
            # for each field (0, x)
            for field_index in range(len(d[group]['_fields_'])):
                # Adding a key to item of the name of the field we are on
                # Setting the value associated with that key to our input
                item[d[group]['_fields_'][field_index]] = input(f"Enter {d[group]['_fields_'][field_index]}: ")
            # Add the dictionary item to the end of the list of data_    
            d[group]['_data_'].append(item)
            print()       
    print()

def list_group_data(d):
    print("** List group data **")
    list_groups(d)

    while True:
        # Get group to list info for
        group = input("Enter group name (empty to cancel): ")
        # If blank end loop
        if group == '':
            break
        # If group does not exist reprompt
        elif group not in d:
            print("Group does not exist")
        
        else:
            # Number of items for printing
            item_num = 0
            # For each item that we stored earlier in data
            for item in d[group]['_data_']:
                # Blank list
                t = []
                # for each key that is in item
                for key, value in item.items():
                    # add to end of blank list the key name and the value associated with the key
                    t.append(f"{key} = {value}")
                # Set item_list equal to a comma delimitted list of the values and keys
                print(f"{item_num} {', '.join(t)}")
                item_num += 1
            print()    
    print()


print(">> Welcome to Group Manager <<")
print("This program creates groups with dynamic properties\n")

d = {}
while True:
    # print(d)
    # Get command
    command = input("Command (empty or X to quit, ? for help): ").strip().upper()
    # Check if command is to exit
    if command == '' or command == 'X':
        break
    # Check if command is for help
    elif command == '?':
        group_help()
    # Check if command is to create new group
    elif command == 'C':
        create_group(d)
    # Check if command is to list groups
    elif command == 'G':
        list_groups(d)
    # Check if command is to add data to a group
    elif command == 'A':
        add_group_data(d)
    # Check if command is to list data in a group
    elif command == 'L':
        list_group_data(d)
