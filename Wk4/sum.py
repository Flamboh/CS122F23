# Write a function that sums up all odd numbers between 2 values

# Write a function that sums up all of the odd or even numbers between 2 values


def sum_odd(start_number, end_number):
    sum = 0
    if start_number % 2 == 0:
        start_number += 1    
    for i in range(start_number, end_number + 1, 2):
        sum += i
    return sum

def sum_odd_or_even(start_number, end_number, parity):
    sum = 0
    if parity == "Odd":  
        if start_number % 2 == 0:
            start_number += 1    
        for i in range(start_number, end_number + 1, 2):
            sum += i
        return sum
    elif parity == "Even":
        if start_number % 2 != 0:
            start_number += 1
        for i in range(start_number, end_number + 1, 2):
            sum += i
        return sum


print(sum_odd_or_even(2, 11, "Odd"))
print(3+5+7+9+11)
print(sum_odd_or_even(2, 11, "Even"))
print(2+4+6+8+10)