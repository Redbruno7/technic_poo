# STUDENT: BRUNO C. RODGERS
# DATE: 13/02/2025
# - Receive 3 values
# - Print sum
# - Print multiplication

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - SUM AND MULTIPLICATION'.center(80))
    print('=' * 80)
    print()


class Operation:
    def __init__(self, a, b, c):
        """
        Initialize class with 3 numbers
        param_1: 1º number
        param_2: 2º number
        param_3: 3º number
        """
        self.a = a
        self.b = b
        self.c = c

    def calculate_sum(self):
        """Return sum 3 values"""
        return f'{self.a} + {self.b} + {self.c} = {self.a + self.b + self.c}'

    def calculate_mult(self):
        """Return multiplication 3 values"""
        return f'{self.a} * {self.b} * {self.c} = {self.a * self.b * self.c}'

    def get_number(self):
        """Iterate method - get 3 values"""
        while True:
            try:
                print('=' * 80)
                self.a = int(input('Enter 1º value: '))
                print('-' * 80)
                self.b = int(input('Enter 2º value: '))
                print('-' * 80)
                self.c = int(input('Enter 3º value: '))
                print('=' * 80)
                print()
                break

            except:
                print('-' * 80)
                print('Invalid value. Try again.')
                print('=' * 80)
                print()


def main():
    cls_term()
    title()

    operations = Operation(0, 0, 0)
    operations.get_number()

    print('=' * 80)
    print('Operations result:')
    print('=' * 80)
    print(f'Sum: {operations.calculate_sum()}')
    print('-' * 80)
    print(f'Multiplication: {operations.calculate_mult()}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
