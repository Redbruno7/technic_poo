# STUDENT: BRUNO C. RODGERS
# DATE: 18/02/2025

import os


def cls_term():
    """Terminal clear
    """    
    os.system('cls')


def title():
    """Title
    """    
    print('=' * 80)
    print('POO - POLIMORFISM / OVERLOAD')
    print('=' * 80)
    print()


class FatherClass:
    def __init__(self, a, b):
        """Initialize 2 attributes

        Args:
            a (int): integer number
            b (int): integer number
        """
        self.a = a
        self.b = b

    def class_method(self, a, b):
        pass


class DaughterClass(FatherClass):
    def __init__(self, a, b):
        """Initialize 2 attributes 

        Args:
            a (int): integer number
            b (int): integer number
        """
        self.a = a
        self.b = b

    def class_method(self):
        """Overload method

        Returns:
            int: sum 2 attributes
        """
        return self.a + self.b


def main():
    """Main software
    """    
    cls_term()
    title()

    teste = DaughterClass(1, 2)
    print('=' * 80)
    print(f'{teste.class_method()}')
    print('=' * 80)


if __name__ == '__main__':
    main()