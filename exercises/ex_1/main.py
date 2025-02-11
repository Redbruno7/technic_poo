# ALUNO: BRUNO C. RODGERS
# Data: 10/02/2025
# Atividade 010 - Letra C - Transformar projeto em OO (Orientado à objeto)

import os


from packs.print import title
from packs.register_system import RegisterSystem

# Limpeza terminal
def cls_terminal():
    os.system('cls')

# Nav
cls_terminal()
title()

# Software
system = RegisterSystem()
system.register_student()

while True:
    print('=' * 80)
    continue_register = input('Deseja cadastrar outro aluno? (s/n): ').strip().lower()
    print('=' * 80)
    print()
    
    if continue_register == 's':
        system.register_student()

    elif continue_register == 'n':
        cls_terminal()
        break
        
    else:
        print('=' * 80)
        print('Resposta inválida. Tente novamente.')
        print('=' * 80)
        print()
        
system.list_students()