# STUDENT: BRUNO C. RODGERS
# DATE: 12/02/2025
# º Create Class in list

import os


def cls_term():
    os.system('cls')

def title():
    print('=' * 80)
    print('POO - CLASS - LIST'.center(80))
    print('=' * 80)
    print()

# Create class "class Class"
class Student:

    # Constructor Method "def __init__(self, param_1, param_2):"
    def __init__(self, name, age):

        # Initiate attributes "self.atb = param"
        self.name = name
        self.age = age
        self.grades = []

    # Function Method "def method(self, param):"
    def add_grade(self, grade):
        self.grades.append(grade)

    # Function Method "def method(self)"
    def media(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    # Void Method "def method(self):"
    def result(self):
        final_media = self.media()
        if final_media >= 7:
            return 'Aprovado.'
        elif final_media >= 5:
            return 'Recuperação.'
        else:
            return 'Reprovado.'

# Void Function "def method(param)"
def show_results(students):
    for student in students:
        print('=' * 80)
        print(f'Name: {student.name}')
        print(f'Age: {student.age}')
        print(f'Media: {student.media():.2f}')
        print(f'Result: {student.result()}')
        print('=' * 80)
        print()

# Function "def function():"
def student_register():
    print('=' * 80)
    name = input('Enter student name: ').strip()
    print('-' * 80)
    age = int(input(f'Enter {name} age: '))
    print('=' * 80)
    print()

    # Call Class "var = Class(arg_1, arg_2)"
    student = Student(name, age)

    print('=' * 80)
    while True:
        try:
            grade = float(input(f'Enter {name} grade ("0" for exit): '))

            if grade == 0:
                print('=' * 80)
                print()
                break

            # Call Class Method "var_class.method(var)"
            student.add_grade(grade)

        except ValueError:
            print('-' * 80)
            print('Invalid grade. Try again.')
            print('-' * 80)

    return student

# Nav
cls_term()
title()

print('=' * 80)
print('Students Register')
print('=' * 80)
print()

student_list = []

while True:
    student = student_register()

    student_list.append(student)

    print('=' * 80)
    continue_register = input('Continue to register (y/n): ').lower()
    print('=' * 80)
    print()

    if continue_register != 'y':
        break

show_results(student_list)