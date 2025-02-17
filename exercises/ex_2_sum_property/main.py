# STUDENT: BRUNO C. RODGERS
# DATE: 17/02/2025

import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('CALCULATE SUM - PROPERTYS')
    print('=' * 80)
    print()


class Sum:
    def __init__(self, a=0, b=0):
        """Initialize 2 attributes

        Args:
            a (int): 1º number. Defaults to 0.
            b (int): 2º number. Defaults to 0.
        """        
        self._a = a
        self._b = b

    @property
    def a(self):
        """Getter

        Returns:
            int: integer number
        """        
        return self._a

    @a.setter
    def a(self, value):
        """Setter

        Args:
            value (int): integer number
        """        
        self._a = value

    @property
    def b(self):
        """Getter

        Returns:
            int: integer number
        """        
        return self._b

    @b.setter
    def b(self, value):
        """Setter

        Args:
            value (int): integer number
        """        
        self._b = value

    @property
    def calculate_sum(self):
        """Calculate method

        Returns:
            int: sum of attributes
        """        
        return self._a + self._b


def main():
    """Main software
    """    
    cls_term()
    title()

    sum = Sum()
    sum.a = 10
    sum.b = 20

    print('=' * 80)
    print(f'{sum.a} + {sum.b} = {sum.calculate_sum}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()