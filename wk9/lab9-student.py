"""
CS 122 Fall 2023 Lab 9 Student
Author: Oliver Boorstein
Credit:
Description: Work with dictionaries
"""

student = {
    'id': '12345678',
    'last_name': 'Doe',
    'first_name': 'John',
    'age': 21,
}
    
# Create empty student list
student_list = []

while True:    
    # Get student ID
    student_id = input("Enter student ID (or '' to quit): ").strip()
    if not student_id:
        break    
    else:
        student['id'] = student_id
    
    # Get student last name
    student_last_name = input("Enter last name: ").strip()
    student['last_name'] = student_last_name

    # Get student first name
    student_first_name = input("Enter first name: ").strip()
    student['first_name'] = student_first_name

    # Get student age
    student_age = input("Enter age: ").strip()
    if not student_age.isdigit():
        print("Invalid age, input set to 0")
        student['age'] = 0
    else:
        student['age'] = int(student_age)
    
    # Add student to student list
    student_list.append(student.copy())

# Print student list
print("\nList of Students:")
for individual in student_list:
    print(individual)
    

