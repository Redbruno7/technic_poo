# STUDENT: BRUNO C. RODGERS
# DATE: 13/02/2025

import os
import math


class Equation:
    def __init__(self, a=1, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    # Getters
    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    # Setters
    def set_a(self, value):
        self._a = value

    def set_b(self, value):
        self._b = value

    def set_c(self, value):
        self._c = value

    def root_calculate(self):
        delta = self._b ** 2 - 4 * self._a * self._c

        if delta < 0:
            return 'The equation has no real roots.'

        elif delta == 0:
            x = self._b / (2 * self._a)
            return f'The equation has one real root: {x}'

        else:
            x_1 = (-self._b + math.sqrt(delta)) / (2 * self._a)
            x_2 = (-self._b - math.sqrt(delta)) / (2 * self._a)
            return f'The equation has two real roots: {x_1} e {x_2}'

os.system('cls')

# Output 1
print('=' * 80)
print('Quadratic equation calculation 1:')
print('=' * 80)
equation_1 = Equation(1, -3, 2)
print(equation_1.root_calculate())
print('=' * 80)
print()

# Output 2
print('=' * 80)
print('Quadratic equation calculation 1:')
print('=' * 80)
equation_1.set_a(1)
equation_1.set_b(2)
equation_1.set_c(1)
print(equation_1.root_calculate())
print('=' * 80)
print()