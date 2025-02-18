# STUDENT: BRUNO C. RODGERS
# DATE: 18/02/2025

import os
from math import pi


def cls_term():
    """Terminal clear
    """    
    os.system('cls')


def title():
    """Title
    """    
    print('=' * 80)
    print('POO - POLIMORFISM')
    print('=' * 80)
    print()


class Form:
    def area(self):
        pass


class Circle(Form):
    def __init__(self, radius):
        """Initialize 1 attribute

        Args:
            radius (int): integer value
        """
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


class Rectangle(Form):
    def __init__(self, base, height):
        """Initialize 2 attributes

        Args:
            base (int): integer value
            height (int): integer value
        """
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)     


def show_area(form):
    print(f'The form area is: {form.area()}')


def main():
    """Main software
    """    
    cls_term()
    title()

    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    square = Square(3)

    print('=' * 80)
    show_area(circle)
    print('-' * 80)
    show_area(rectangle)
    print('-' * 80)
    show_area(square)
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()