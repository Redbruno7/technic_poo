# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive base and height rectangle;
# - Calculate perimeter

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - CALCULATE RECTANGLE PERIMETER'.center(80))
    print('=' * 80)
    print()


class RectanglePerimeter():
    def __init__(self, base=0, height=0):
        """
        Initialize 2 float values
        param_1: base
        param_2: height
        """
        self.base = base
        self.height = height

    def get_values(self):
        """
        Iterate method: get base and height
        """
        while True:
            try:
                print('=' * 80)
                self.base = float(input('Enter base: '))

                if self.base > 0:
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

        while True:
            try:
                print('-' * 80)
                self.height = float(input('Enter height: '))

                if self.height > 0:
                    print('=' * 80)
                    print()
                    break
                else:
                    print('-' * 80)
                    print('Invalid value. Try again.')

            except ValueError:
                print('-' * 80)
                print('Invalid input. Try again.')

    def calculate_perimeter(self):
        """
        Calculate method: Return rectangle perimeter
        """
        return (self.base * 2) + (self.height * 2)


def main():
    cls_term()
    title()

    rectangle_perimeter = RectanglePerimeter()
    rectangle_perimeter.get_values()

    print('=' * 80)
    print(
        f'Rectangle perimeter: {rectangle_perimeter.calculate_perimeter():.2f}'
        )
    print('=' * 80)
    print()



if __name__ == '__main__':
    main()
