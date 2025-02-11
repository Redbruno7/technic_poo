class Student:
    def __init__(self, name, register, birth):
        self.name = name
        self.register = register
        self.birth = birth

    def show_data(self):
        print('=' * 80)
        print(f'Nome: {self.name}')
        print(f'Matrícula: {self.register}')
        print(f'Nascimento: {self.birth}')
        print('=' * 80)
        print()