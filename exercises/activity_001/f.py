# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Convert m to cm;
# - Convert cm to mm;

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - MEASUREMENT CONVERSION'.center(80))
    print('=' * 80)
    print()


class MeasurementConversion:
    def __init__(self, a=0):
        """
        Initialize 1 measurement
        param_1 = m value
        """
        self.a = a

    def get_m(self):
        """Iterate method - get m value"""
        while True:
            try:
                print('=' * 80)
                self.a = float(input('Enter in meters: '))
                if self.a > 0:
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
                print('Invalid value. Try again.')
                print('=' * 80)
                print()

    def convert(self):
        """
        Processual method
        1: return conversion m to cm
        2: return conversion cm to mm
        """
        return self.a * 100, self.a * 1000


def main():
    cls_term()
    title()

    number = MeasurementConversion()
    number.get_m()
    cm, mm = number.convert()

    print('=' * 80)
    print(f'M to cm: {cm}')
    print('-' * 80)
    print(f'Cm to mm: {mm}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
