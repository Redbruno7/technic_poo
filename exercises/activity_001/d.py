# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive 2 numbers
# - Calculate division (format: 4 decimal places)

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - CALCULATE DIVISION'.center(80))
    print('=' * 80)
    print()


class Division:
    def __init__(self, a=0, b=0):
        """
        Initialize 2 numbers
        param_1: 1º number
        param_2: 2º number
        """
        self.a = a
        self.b = b

    def get_numbers(self):
        """Iterate method - get 2 numbers"""
        while True:
            try:
                print('=' * 80)
                self.a = float(input('Enter 1º number: '))
                print('-' * 80)
                self.b = float(input('Enter 2º number: '))
                print('=' * 80)
                print()
                break
            except ValueError:
                print('-' * 80)
                print('Invalid number. Try again.')
                print('=' * 80)
                print()

    def calculate_div(self):
        """Calculate method - return division"""
        return self.a / self.b


def main():
    cls_term()
    title()

    division = Division()
    division.get_numbers()

    print('=' * 80)
    print(f'Result: {division.calculate_div():.4f}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
