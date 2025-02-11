# STUDENT: BRUNO C. RODGERS
# DATE: 11/02/2025
# º Create Class

import os


def cls_term():
    os.system('cls')

def title():
    print('=' * 80)
    print('POO - CLASS'.center(80))
    print('=' * 80)
    print()

# Create class "class Class"
class Vehicle:

    # Constructor Method "def __init__(self, a, b, c, d)"
    def __init__(self, brand, model, year, color):

        # Initiate attributes "self.atb = param"
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

# Nav
cls_term()
title()

# Software
print('=' * 80)
brand = input('Enter vehicle brand: ').strip()
print('-' * 80)
model = input('Enter vehicle model: ').strip()
print('-' * 80)
year = input('Enter vehicle year: ').strip()
print('-' * 80)
color = input('Enter vehicle color: ').strip()
print('=' * 80)
print()

# Create object from class "var = Class(value_1, value_2, value_3, value_4)"
vehicle_1 = Vehicle(brand, model, year, color)

# Output
print('=' * 80)
print('Vehicle Information:')
print('-' * 80)
print(f'Brand: {vehicle_1.brand}')
print(f'Model: {vehicle_1.model}')
print(f'Year: {vehicle_1.year}')
print(f'Color: {vehicle_1.color}')
print('=' * 80)
print()