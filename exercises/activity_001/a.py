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
    print('POO - SUM AND MULTIPLICATION')
    print('=' * 80)
    print()


class Operation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_sum(self, a, b, c):
        self.sum = self.a + self.b + self.c
        return self.sum

    def calculate_mult(self, a, b, c):
        self.multiply = self.a * self.b * self.c
        return self.multiply

    def get_number(self):
        while True:
            try:
                print('=' * 80)
                self.a = int(input('Enter 1º value: '))
                print('-' * 80)
                self.b = int(input('Enter 2º value: '))
                

            except:
                print('-' * 80)
                print('Invalid value. Try again.')
                print('-' * 80)


def main():
    cls_term()
    title()

    numbers = Operation.get_number()

    print(f'{numbers}')

if __name__ == '__main__':
    main()