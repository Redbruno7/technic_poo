# STUDENT: BRUNO C. RODGERS
# DATE: 11/02/2025
# º Create Class with CSV file

import os
import csv


def cls_term():
    os.system('cls')

def title():
    print('=' * 80)
    print('POO - CLASS - CSV'.center(80))
    print('=' * 80)
    print()

# Create class "class Class"
class BankAccount:

    # Constructor Method "def __init__(self, param_1, param_2, param_3, param_4, param_5):"
    def __init__(
        self, account_number, holder_name, balance, branch, account_type
        ):

        # Initiate attributes "self.atb = param"
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.branch = branch
        self.account_type = account_type

# Function method - create instance class
def get_account_data():
    print('=' * 80)
    account_number = input('Enter account number: ')
    print('-' * 80)
    holder_name = input('Enter holder account name: ')
    print('-' * 80)
    balance = float(input('Enter initial balance: '))
    print('-' * 80)
    branch = input('Enter branch: ')
    print('-' * 80)
    account_type = input('Enter account type: ')
    print('=' * 80)
    print()
    return BankAccount(
        account_number, holder_name, balance, branch, account_type
        )

# Nav
cls_term()
title()

# Input
account_list = []

# Software
while True:
    account = get_account_data()
    account_list.append({
        'account_number': account.account_number,
        'holder_name': account.holder_name,
        'balance': account.balance,
        'branch': account.branch,
        'account_type' : account.account_type
    })

    print('=' * 80)
    continue_register = input('Continue to register (y/n): ').lower()
    print('=' * 80)
    print()

    if continue_register != 'y':
        break

# Path to folder CSV file will be saved "var = 'path'"
folder = 'arquivos_csv/conta/'

# Verify folder existence, if not will be create "os.makedirs(var, exist_ok = True)"
os.makedirs(folder, exist_ok = True)

# File name to CSV file record informations "var = 'path.csv'"
file = 'arquivos_csv/conta/conta.csv'

# Enter list dicts in CSV file "with open(var_1, mode = 'w', newline = '') as var_2"
with open(file, mode = 'w', newline = '') as account:
    fieldnames = [
        'account_number',
        'holder_name',
        'balance',
        'branch',
        'account_type'
        ]

    writer = csv.DictWriter(account, fieldnames = fieldnames, delimiter = ';')

    writer.writeheader()
    for register in account_list:
        writer.writerow(register)

print('=' * 80)
print(f'The data account were saved in {file}')
print('=' * 80)
print()