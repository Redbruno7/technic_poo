# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive integer number;
# - Print multiplicationtable.

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - '.center(80))
    print('=' * 80)
    print()

class MultiplicationTable:
    def __init__(self, a=0):
        """
        Initialize 1 integer number
        param_1: 1 integer number
        """
        self.a = a

    def get_number(self):
        """
        Iterate method - get number
        """
        while True:
            try:
                print('=' * 80)
                self.a = int(input('Enter number: '))
                print('=' * 80)
                print()
                break
            except:
                print('-' * 80)
                print('Invalid number. Try again.')
                print('=' * 80)
                print()

    def calculate_mult_table(self):
        """
        Calculate method - Return list multiplication table
        """
        list_mult_table = []
        for i in range(1, 10):
            list_mult_table.append(f'{self.a} * {i} = {self.a * i}')
        return list_mult_table


def main():
    cls_term()
    title()

    multiplication_table = MultiplicationTable()
    multiplication_table.get_number()

    print('=' * 80)
    for i in multiplication_table.calculate_mult_table():
        print(f'{i}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
