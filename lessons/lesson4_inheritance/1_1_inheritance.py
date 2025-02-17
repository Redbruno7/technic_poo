# STUDENT: BRUNO C. RODGERS
# DATE: 17/02/2025

import os


def cls_term():
    """Terminal clear
    """    
    os.system('cls')


def title():
    """Title
    """    
    print('=' * 80)
    print('POO - INHERITANCE')
    print('=' * 80)
    print()


class Animal:
    def __init__(self, name):
        """Initialize 1 attribute

        Args:
            name (string): animal name
        """        
        self.name = name

    def bark(self):
        """Return string

        Returns:
            string: text direct
        """        
        return 'This in the bark method()'

    def meow(self):
        """Return string

        Returns:
            string: text direct
        """        
        return 'This in the meow method()'


class Dog(Animal):
    def bark(self):
        """Action method

        Returns:
            string: continuous action
        """        
        return f'{self.name} is barking.'
    

class Cat(Animal):
    def meow(self):
        """Action method

        Returns:
            string: continuous action
        """        
        return f'{self.name} is meowing.'


def main():
    """Main software
    """    
    cls_term()
    title()

    dog = Dog('Rex')
    cat = Cat('Tobias')

    print('=' * 80)
    print(dog.bark())
    print(cat.meow())
    print('=' * 80)
    print()


if __name__ == '__main__':
    main()