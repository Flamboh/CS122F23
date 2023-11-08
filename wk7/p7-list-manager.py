"""
CS 122 Fall 2023 Project 7 List Manager
Author: Oliver Boorstein
Credit:
Description: 
"""

def cmd_help():
    cmds = ["Add", "Delete", "List", "Clear"]
    cmds_desc =["Add to list", "Delete information", "List information", "Clear"]
    cmd_spacing = get_max_list_item_size(cmds) + 5

    for i in range(4):
        print(pad_right(cmds[i], cmd_spacing), pad_right(cmds_desc[i], 5))
    print("Empty to exit")


def cmd_add(t):
    while True:
        item_to_add = input("Enter information (empty to stop): ").strip()
        if item_to_add == "":
            break
        else:
            t.append(item_to_add)
            print(f"Added, item count = {len(t)}")

def cmd_delete(t):
    while True:        
        for i in range(len(t)):
            pad_amount = len(str(i)) + 2
            print(f"{pad_right(i, pad_amount)}{t[i]}")
        index = input("Enter number to delete (empty to stop): ").strip()
        if index == "":
            break
        elif not index.isdigit():
            print("Input must be integer")
        elif not int(index) in range(len(t)):
            print("Input must be within size of list")
        else:
            t.pop(int(index))
        
        if len(t) == 0:
            print("All items deleted")
            break

def cmd_list(t):
    print(f"List contains {len(t)} item(s)")
    for item in t:
        print(item)

def cmd_clear(t):
    print(f"{len(t)} item(s) removed, list empty")
    t.clear() 

def get_max_list_item_size(t):
    result = 0
    for s in t:
        if len(s) > result:
            result = len(s)

    return result


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

managed_list = []

while True:
    command = input("Enter a command (? for help): ").strip().lower()
    if command == "":
        break
    elif command == "?":
        cmd_help()
    elif command == "add":
        cmd_add(managed_list)
    elif command == "del":
        cmd_delete(managed_list)
    elif command == "clear":
        cmd_clear(managed_list)
    elif command == "list":
        cmd_list(managed_list)

print("Goodbye!")