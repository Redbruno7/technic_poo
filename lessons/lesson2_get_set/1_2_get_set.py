# STUDENT: BRUNO C. RODGERS
# DATE: 13/02/2025

import os
from datetime import datetime


class User:
    def __init__(self, name, birth):

        # Call settet to set
        self.set_name(name)
        self.set_birth(birth)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_birth(self):
        return self._birth

    def set_birth(self, birth):
        self._birth = birth

        today = datetime.now()

        birthday = datetime.strptime(birth, '%d/%m/%Y')

        self._age = today.year - birthday.year - \
            ((today.month, today.day) < (birthday.month, birthday.day))

    def get_age(self):
        return self._age

os.system('cls')

print('=' * 80)
print('Age Calculate:')
print('=' * 80)
print()

print('=' * 80)
name = input('Enter name: ').strip()
print('-' * 80)
birth = input('Enter birth (dd/mm/yyyy): ')
print('=' * 80)
print()

user = User(name, birth)

print('=' * 80)
print(f'Name: {user.get_name()}')
print(f'Birthday: {user.get_birth()}')
print(f'Age: {user.get_age()} years')
print('=' * 80)
print()