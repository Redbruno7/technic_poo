import os


from packs.student import Student

class RegisterSystem:
    def __init__(self):
        self.students = []

    def register_student(self):
        print('=' * 80)
        while True:
            name = input('Digite o nome do aluno: ').strip()
            print('-' * 80)

            if name:
                break

            print('Nome inválido. Tente novamente.')
            print('-' * 80)

        while True:
            register = input('Digite a matrícula do aluno: ').strip()
            print('-' * 80)

            if register.isdigit():
                register = int(register)
                break

            print('Matrícula inválida. Tente novamente.')
            print('-' * 80)

        while True:
            birth = input(
                'Digite a data de nascimento do aluno (dd/mm/aaaa): ').strip()

            if len(birth) == 10 and birth[
                2
                ] == '/' and birth[
                    5
                    ] == '/' and birth.replace('/', '').isdigit():
                break

            print('-' * 80)
            print('Data de nascimento inválida. Tente no formato (dd/mm/aaaa).')
            print('-' * 80)

        student = Student(name, register, birth)
        self.students.append(student)
        print('=' * 80)
        print()

    def list_students(self):
        if not self.students:
            print('=' * 80)
            print('Cadastre um aluno primeiro.')
            print('=' * 80)
            print()
            return

        print('=' * 80)
        print('Alunos cadastrados:')
        print('=' * 80)
        print()
        
        for student in self.students:
            student.show_data()