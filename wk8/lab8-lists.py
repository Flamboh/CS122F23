"""
CS 122 Fall 2023 Lab 8 Lists
Author: Oliver Boorstein
Credit:
Description: Learn about lists
"""

import random

def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
    """
    Generates a list of random integers with a given size and range and sorting and returns the list
    """
    # Declare list
    t = []

    # Check if the size of list is > 0
    if num <= 0:
        print('num must be > 0')
    # Check if num is an integer
    elif not isinstance(num, int):
        print('num must be an integer')
    # Check if the range numbers are integers
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
        print('start_range and end_range must be integers')
    # If inputs are appropriate generate the list
    else:
        for i in range(num):
            # Generate a number between the range
            r = random.randint(start_range, end_range)
            #put the number at the end of the list
            t.append(r)

        # If sort_list variable is Y then order the list numerically
        if sort_list.upper() == 'Y':
            t.sort()

    return t

def get_high_score(t):
    score_list = t
    result = 0
    if not isinstance(t, list):
        print("List argument expected")
        result = -1
    elif not t:
        result = 0
    else:
        score_list.sort()
        result = score_list[-1]
    
    return result

def get_low_score(t):
    score_list = t
    result = 0
    if not isinstance(score_list, list):
        print("List argument expected")
        result = -1
    elif not score_list:
        result = 0
    else:
        score_list.sort()
        result = score_list[0]
    
    return result

def get_mean_score(t):
    score_list = t
    result = 0
    if not isinstance(score_list, list):
        print("List argument expected")
        result = -1
    elif not score_list:
        result = 0
    else:
        result = round(int(sum(score_list)) / len(score_list), 2)
        
    return result    

def get_median_score(t):
    score_list = t
    result = 0
    if not isinstance(score_list, list):
        print("List argument expected")
        result = -1
    elif not score_list:
        result = 0
    elif len(score_list) == 1:
        result = score_list[0]
    elif len(score_list) % 2 == 0:
        # Find middle 2 elements
        a = int((len(score_list)/2) - 1)
        b = a + 1
        result = (score_list[a] + score_list[b]) / 2
    elif not len(score_list) % 2 == 0:
        # Find middle element
        a = int(len(score_list)/2)
        result = score_list[a]
    return result    

def count_range(t, low_score, high_score):
    score_list = t
    result = 0
    if not isinstance(t, list):
        print("List argument expected")
        result = -1
    elif not isinstance(low_score, int) or not isinstance(high_score, int):
        print("Start and end must be integers")
        result = -1
    elif low_score >= high_score:
        print("Start must be < end")
        result = -1
    elif not score_list:
        result = 0
    else:
        for i in score_list:
            if i >= low_score and i <= high_score:
                result += 1
    return result

def list_range(t):
    score_list = t
    print(f"A - {count_range(score_list, 90, 100)}")
    print(f"B - {count_range(score_list, 80, 89)}")
    print(f"C - {count_range(score_list, 70, 79)}")
    print(f"D - {count_range(score_list, 60, 69)}")
    print(f"F - {count_range(score_list, 0, 59)}")

t = gen_random_integer_list(100)

b = [1,2,3,4,5]

print(get_high_score(t))
print(get_low_score(t))
print(get_mean_score(t))
print(get_median_score(t))
list_range(t)