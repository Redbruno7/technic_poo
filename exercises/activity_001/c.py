# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive 4 grades
# - Calculate media

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - CALCULATE MEDIA')
    print('=' * 80)
    print()


class Student:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_grade(self):
        while True:
            try:
                print('=' * 80)
                self.a = float(input('Enter 1º grade: '))
                print('-' * 80)
                self.b = float(input('Enter 2º grade: '))
                print('-' * 80)
                self.c = float(input('Enter 3º grade: '))
                print('-' * 80)
                self.d = float(input('Enter 4º grade: '))
                print('=' * 80)
                print()
                break
            except:
                print('-' * 80)
                print('Invalid grade. Try again.')
                print('=' * 80)
                print()

    def calculate_media(self):
        return (self.a + self.b + self.c + self.d) / 4


def main():
    cls_term()
    title()

    student = Student()
    student.get_grade()

    print('=' * 80)
    print(f'Media: {student.calculate_media():.2f}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
