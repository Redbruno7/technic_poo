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
class Bank:

    # Constructor Method "def __init__(self, param_1 = '', param_2 = 0, param_3 = 0, param_4 = 0, param_5 = 0, param_6 = 0)"
    def __init__(self, name = '', branch = 0, account = 0, cpf = 0,
                 checking_account = 0, saving_account = 0):

        # Initiate attributes "self.atb = param"
        self.name = name
        self.branch = branch
        self.account = account
        self.cpf = cpf
        self.checking_account = checking_account
        self.saving_account = saving_account

    # Function method "def function(self, param)"
    def deposit(self, value):
        print('=' * 80)
        choice = input(
            'Checking Account (CA) or Saving Account (SA): '
            ).lower().strip()

        if choice == 'ca':
            print('=' * 80)
            print(f'Deposit amount: (+) R$ {value}')
            print(f'Previous balance (CA): R$ {self.checking_account}')

            self.checking_account += value

            print(f'Current balance (CA): R$ {self.checking_account}')
            print('=' * 80)
            print()

        elif choice == 'sa':
            print('=' * 80)
            print(f'Deposit amount: (+) R$ {value}')
            print(f'Previous balance (SA): R$ {self.saving_account}')

            self.saving_account += value

            print(f'Current balance (SA): R$ {self.saving_account}')
            print('=' * 80)
            print()

        else:
            print('-' * 80)
            print('Invalid option. Try again.')
            print('-' * 80)

    # Function method "def function(self, param)"
    def withdraw(self, value):
        print('=' * 80)
        choice = input(
            'Checking Account (CA) or Saving Account (SA): '
            ).lower().strip()

        if choice == 'ca':
            print('=' * 80)
            print(f'Withdraw amount: (+) R$ {value}')
            print(f'Previous balance (CA): R$ {self.checking_account}')

            self.checking_account += value

            print(f'Current balance (CA): R$ {self.checking_account}')
            print('=' * 80)
            print()

        elif choice == 'sa':
            print('=' * 80)
            print(f'Withdraw amount: (-) R$ {value}')
            print(f'Previous balance (SA): R$ {self.saving_account}')

            self.saving_account += value

            print(f'Current balance (SA): R$ {self.saving_account}')
            print('=' * 80)
            print()

        else:
            print('-' * 80)
            print('Invalid option. Try again.')
            print('-' * 80)

# Nav
cls_term()
title()

# Input
print('=' * 80)
print('Create a new account:')
print('-' * 80)
name = input('Enter name: ')
print('-' * 80)
branch = int(input('Enter branch: '))
print('-' * 80)
account = int(input('Enter account number: '))
print('-' * 80)
cpf = int(input('Enter CPF: '))
print('-' * 80)
checking_account = float(input('Enter initial checking account balance: '))
print('-' * 80)
saving_account = float(input('Enter initial saving account balance: '))
print('=' * 80)
print()

# Create object from class "var = Class(value_1, value_2, value_3, value_4, value_5, value_6)"
holder = Bank(name, branch, account, cpf, checking_account, saving_account)

# Iterate
print('=' * 80)
print('Financial Transaction')
print('-' * 80)
option = input('Deposit or Withdrawal (D/W): ').upper().strip()
print('=' * 80)
print()

# Software
if option == 'D':
    print('=' * 80)
    value = float(input('Deposit amount: '))
    print('=' * 80)
    print()

    # Call Class method "var.method(arg)"
    holder.deposit(value)

elif option == 'S':
    print('=' * 80)
    value = float(input('Withdraw amount: '))

    # Call Class method "var.method(arg)"
    holder.withdraw(value)

else:
    print('=' * 80)
    print('Invalid Option. Try again.')
    print('=' * 80)
    print()