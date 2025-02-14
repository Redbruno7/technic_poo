# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive 1 int number
# - Print predecessor em successor
# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - PREDECESSOR AND SUCCESSOR'.center(80))
    print('=' * 80)
    print()


class IntegerNumber:
    def __init__(self, a=0):
        """
        Initialize 1 int number
        param_1: int number
        """
        self.a = a

    def get_number(self):
        """Iterate method - get 1 number"""
        while True:
            try:
                print('=' * 80)
                self.a = int(input('Enter number: '))
                print('=' * 80)
                print()
                break
            except ValueError:
                print('-' * 80)
                print('Invalid number. Try again.')
                print('=' * 80)
                print()

    def get_pred_suc(self):
        """processual method - return predecessor and successor"""
        return self.a - 1, self.a + 1


def main():
    cls_term()
    title()

    number = IntegerNumber()
    number.get_number()
    pred, suc = number.get_pred_suc()

    print('=' * 80)
    print(f'Predecessor: {pred}')
    print(f'Successor: {suc}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
