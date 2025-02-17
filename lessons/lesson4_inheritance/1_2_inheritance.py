# STUDENT: BRUNO C. RODGERS
# DATE: 17/02/2025

import os
import math


def cls_term():
    """Terminal clear
    """    
    os.system('cls')


def title():
    """Title
    """    
    print('=' * 80)
    print('POO - INHERITANCE')
    print('=' * 80)
    print()


class Triangle:
    def __init__(self, adjacent_cathet, oppost_cathet):
        """Initialize 2 cathets

        Args:
            adjacent_cathet (float): adjacent cathet value
            oppost_cathet (float): oppost cathet value
        """        
        self.adjacent_cathet = adjacent_cathet
        self.oppost_cathet = oppost_cathet


class RightTriangle(Triangle):
    def hypotenuse_calculate(self):
        """Calculate method

        Returns:
            float: hypotenuse value
        """        
        result = math.sqrt(
            pow(self.adjacent_cathet, 2) + pow(self.oppost_cathet, 2)
            )
        return result


def main():
    """Main software
    """    
    while True:
        cls_term()
        title()
        print('=' * 80)
        adjacent_cathet = float(input('Enter adjacent cathet: '))
        print('-' * 80)
        oppost_cathet = float(input('Enter oppost cathet: '))
        print('=' * 80)
        print()

        if adjacent_cathet == 0 or oppost_cathet == 0:
            print('=' * 80)
            print('Software ended.')
            print('=' * 80)
            print()
            break
        else:
            right_triangle = RightTriangle(adjacent_cathet, oppost_cathet)
            hypotenuse = right_triangle.hypotenuse_calculate()

            print('=' * 80)
            print(f'The right triangle with side 1 = {adjacent_cathet} and '
                f'side 2 = {oppost_cathet} it has a hypotenuse = {hypotenuse:.2f}')
            print('=' * 80)
            print()

            print('=' * 80)
            input('Enter to continue: ')


if __name__ == '__main__':
    main()