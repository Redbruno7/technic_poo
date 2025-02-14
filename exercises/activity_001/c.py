# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive 4 grades
# - Calculate media

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - CALCULATE MEDIA'.center(80))
    print('=' * 80)
    print()


class Student:
    def __init__(self, a=0, b=0, c=0, d=0):
        """
        Initialize 4 grades
        param_1: 1º grade
        param_2: 2º grade
        param_3: 3º grade
        param_4: 4º grade
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_grade(self):
        """Iterate method - get 4 grades"""
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
                if all(
                    0 <= grade <= 10 for grade in [
                        self.a, self.b, self.c, self.d
                        ]):
                    break
                else:
                    print('-' * 80)
                    print('Grades must be between 0-10. Try again.')
                    print('=' * 80)
                    print()
            except ValueError:
                print('-' * 80)
                print('Invalid grade. Try again.')
                print('=' * 80)
                print()

    def calculate_media(self):
        """Calculate method - Return media"""
        return (self.a + self.b + self.c + self.d) / 4


def main():
    """Main software"""
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
