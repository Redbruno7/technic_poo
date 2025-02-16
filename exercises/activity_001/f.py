# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive 1 float number;
# - Calculate double and triple.

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - CALCULATE DOUBLE AND TRIPLE'.center(80))
    print('=' * 80)
    print()


class Operations:
    def __init__(self, a = 0):
        """
        Initialize 1  float number
        param_1: float number
        """
        self.a = a

    def get_number(self):
        """
        Iterate method - get float number
        """
        while True:
            try:
                print('=' * 80)
                self.a = float(input('Enter number: '))
                print('=' * 80)
                print()
                break
            except ValueError:
                print('-' * 80)
                print('Invalid number. Try again.')
                print('=' * 80)
                print()

    def calculate_double(self):
        """
        Calculate method - a * 2
        """
        return self.a * 2

    def calculate_triple(self):
        """
        Calculate melhor - a * 3
        """
        return self.a * 3


def main():
    cls_term()
    title()

    operations = Operations()
    operations.get_number()

    print('=' * 80)
    print(f'Result double: {operations.calculate_double()}')
    print('-' * 80)
    print(f'Result triple: {operations.calculate_triple()}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
