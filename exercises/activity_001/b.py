# STUDENT: BRUNO C. RODGERS
# DATE: 14/02/2025
# - Receive year birth.
# - Calculate age.

import os
import datetime


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - CALCULATE AGE')
    print('=' * 80)
    print()


class Person:
    def __init__(self, year_birth=0):
        """
        Initialize 1 attribute
        param_1 : year birth
        """
        self.year_birth = year_birth

    def get_age(self):
        """Iterate method - get age"""
        while True:
            try:
                print('=' * 80)
                self.year_birth = int(input('Enter year birth: '))

                if self.year_birth <= datetime.datetime.now().year:
                    break

                else:
                    print('-' * 80)
                    print('Invalid year. Try again.')

                print('=' * 80)
                print()

            except:
                print('-' * 80)
                print('Invalid input. Try again.')
                print('=' * 80)
                print()

    def calculate_age(self):
        """Return age calculation"""
        self.current_year = datetime.datetime.now().year
        return self.current_year - self.year_birth


def main():
    cls_term()
    title()

    person_1 = Person()
    person_1.get_age()

    print('=' * 80)
    print(f'Age: {person_1.calculate_age()} years.')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()
