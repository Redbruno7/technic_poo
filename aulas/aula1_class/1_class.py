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

# Data input
def get_data():
    data_dict = {}
    print('=' * 80)
    name = input('Enter name: ').strip()
    data_dict['name'] = name
    print('-' * 80)
    cpf = input('Enter cpf: ').strip()
    data_dict['cpf'] = cpf
    print('-' * 80)
    birth = input('Enter birth: ').strip()
    data_dict['birth'] = birth
    print('-' * 80)
    cep = input('Enter cep: ').strip()
    data_dict['cep'] = cep
    print('-' * 80)
    city = input('Enter city: ').strip()
    data_dict['city'] = city
    print('-' * 80)
    state = input('Enter state: ').strip()
    data_dict['state'] = state
    print('=' * 80)
    print()

    return data_dict

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

data_list = []

# Software
data_list.append(get_data())

print('=' * 80)
for i in data_list:
    for key,value in i.items():
        print(f'{key}: {value}')
print('=' * 80)
print()

teste