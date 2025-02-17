# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive 1 value real;
# - Calculate how many Dolars to buy with this amount.

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - CAMBIO REAL TO DOLAR'.center(80))
    print('=' * 80)
    print()


class Cambio:
    def __init__(self, real=0):
        """
        Initialize 1 attribute
        param_1: BR$
        """
        self.real = real

    def get_value(self):
        """
        Iterate method - get value
        """
        while True:
            try:
                print('=' * 80)
                self.real = float(input('Enter value: '))

                if self.real > 0:
                    print('=' * 80)
                    print()
                    break

                else:
                    print('-' * 80)
                    print('Invalid value. Try again.')
                    print('=' * 80)
                    print()

            except ValueError:
                print('-' * 80)
                print('Invalid input. Try again.')
                print('=' * 80)
                print()

    def convert_value(self):
        """
        Calculate method - BR$ to Dolar
        1: Return dolars
        2: Return change
        """
        return self.real / 5.70


def main():
    cls_term()
    title()

    cambio = Cambio()
    cambio.get_value()

    print('=' * 80)
    print(f'You can buy $ {cambio.convert_value():.2f} Dolars.')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
