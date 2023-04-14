'''
Section 3: Python Challenge [25 marks]
You are tasked with calcualting the minimum classes we need to have so we know how
many people to employ. Write a function which when given a number of students, 
calculates and prints out a string for your proposed number of classes, and a dictionary
showing the allocation.

Key constrains: 
- The maximum size of a class is 30 
- There needs to be a minimum of 2 classes
- The distribution of each class should be as even as possible
- we want to hire as little people as possible - so where possible focus on bigger 
classes, and less of them!

example: 
if 31 was the input, the output would be: 
    proposed allocation : 2 classes 
    {"Class 1": 16, "Class 2: 15}

example: 
if 59 was the input, the output would be: 
    proposed allocation: 2 classes
    {'class 1': 29, 'class 2': 29 'class 3': 29}
    '''

def allocate_classes(total_students):
    max_class_size = 30
    min_num_classes = 2

    num_classes = max(min_num_classes, (total_students) // max_class_size + 1)

    students_per_class = total_students // num_classes

    remaining_students = total_students % num_classes

    allocation = {}
    for i in range(num_classes):
        class_size = students_per_class + (i < remaining_students)
        allocation[f"Class {i + 1}"] = class_size

    print(f"Proposed allocation: {num_classes} classes")
    print(allocation)
    return allocation

done