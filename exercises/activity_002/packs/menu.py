import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - VEHICLE REGISTER SYSTEM'.center(80))
    print('=' * 80)
    print()


def menu_1():
    print('=' * 80)
    print('Menu:'.center(80))
    print('=' * 80)
    print('1. Register vehicle.')
    print('2. Modify register.')
    print('3. Delete register.')
    print('4. Show registers.')
    print('5. Exit.')
    print('-' * 80)


def menu_2():
    print('=' * 80)
    print('Especify Menu:'.center(80))
    print('=' * 80)
    print('1. Car.')
    print('2. Motorcycle.')
    print('3. Truck.')
    print('4. Back.')
    print('-' * 80)