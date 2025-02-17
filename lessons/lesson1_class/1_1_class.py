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
class Person:

    # Constructor Method "def __init__(self, a, b, c, d, e, f)"
    def __init__(self, name, cpf, birth, cep, city, state):

        # Initiate attributes "self.atb = param"
        self.name = name
        self.cpf = cpf
        self.birth = birth
        self.cep = cep
        self.city = city
        self.state = state

# Nav
cls_term()
title()

# Software
print('=' * 80)
name = input('Enter name: ').strip()
print('-' * 80)
cpf = input('Enter cpf: ').strip()
print('-' * 80)
birth = input('Enter birth: ').strip()
print('-' * 80)
cep = input('Enter cep: ').strip()
print('-' * 80)
city = input('Enter city: ').strip()
print('-' * 80)
state = input('Enter state: ').strip()
print('=' * 80)
print()

# Create object from class "var = Class(value_1, value_2, value_3, value_4, value_5, value_6)"
person_1 = Person(name, cpf, birth, cep, city, state)

# Output
print('=' * 80)
print('Person Information:')
print('-' * 80)
print(f'Name: {person_1.name}')
print(f'CPF: {person_1.cpf}')
print(f'Birth: {person_1.birth}')
print(f'CEP: {person_1.cep}')
print(f'City: {person_1.city}')
print(f'State: {person_1.state}')
print('=' * 80)
print()