# STUDENT: BRUNO C. RODGERS
# DATE: 17/02/2025

import os


def cls_term():
    os.system('cls')

# Get - Set
class MyClass:
    def __init__(self, value):
        """Initialize 1 attribute

        Args:
            value (int): integer number
        """        
        self._attribute = value

    def get_attribute(self):
        """Getter

        Returns:
            int: integer number
        """        
        return self._attribute

    def set_attribute(self, value):
        """Setter

        Args:
            value (int): integer number
        """        
        self._attribute = value

# Properties
class MyClass2:
    def __init__(self, value):
        """Initialize 1 attribute

        Args:
            value (int): integer number
        """        
        self._attribute = value

    @property
    def attribute(self):
        """Getter

        Returns:
            int: integer number
        """        
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        """Setter

        Args:
            value (int): integer number
        """        
        self._attribute = value


def main():
    """Main software
    """    
    cls_term()
    obj = MyClass(10)
    obj.set_attribute(20)

    print('=' * 80)
    print(f'Output 1: {obj.get_attribute()}')
    print('=' * 80)
    print()

    obj_2 = MyClass2(10)
    obj_2.attribute = 20

    print('=' * 80)
    print(f'Output 2: {obj_2.attribute}')
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()