from packs.menu import cls_term, title, menu_1, menu_2
from packs.classes import Car, Motorcycle, Truck


def main_menu():
    while True:
        cls_term()
        title()
        menu_1()

        option = input('Choose option (1-5): ')

        if option.isdigit():
            option = int(option)

            if option == 1:
                cls_term()
                title()
                register_menu()
            elif option == 2:
                cls_term()
                title()
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                print('=' * 80)
                print()
                print('=' * 80)
                print('Shutting down system.')
                print('=' * 80)
                print()
                break
            else:
                print('-' * 80)
                input('Invalid option. Press enter to try again: ')
                cls_term()

        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()


def register_menu():
    while True:
        menu_2()

        option = input('Choose option (1-4): ').strip()

        if option.isdigit():
            option = int(option)

            if option == 1:
                while True:
                    cls_term()
                    title()
                    register_car()
                    print()
                    register_again()

            elif option == 2:
                while True:
                    cls_term()
                    title()
                    register_motorcycle()
                    print()
                    register_again()

            elif option == 3:
                while True:
                    cls_term()
                    title()
                    register_truck()
                    print()
                    register_again()

            elif option == 4:
                return

            else:
                print('-' * 80)
                input('Invalid option. Press enter to try again: ')
                cls_term()

        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()


def register_car():
    car = Car()

    print('=' * 80)
    while True:
        try:
            car.get_data()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('=' * 80)
    print('Car registered successfully.')
    return car.car_data()


def register_motorcycle():
    motorcycle = Motorcycle()

    print('=' * 80)
    while True:
        try:
            motorcycle.get_data()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('=' * 80)
    print('Motorcycle registered successfully.')
    return motorcycle.motorcycle_data()


def register_truck():
    truck = Truck()

    print('=' * 80)
    while True:
        try:
            truck.get_data()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('=' * 80)
    print('Truck registered successfully.')
    return truck.truck_data()


def register_again():
    print('=' * 80)
    while True:
        register_again = input(
            'Continue register (y/n): '
        ).strip().lower()

        if register_again == 'n':
            return menu()
        elif register_again == 'y':
            cls_term()
            title()
            return register_menu()
        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            print('-' * 80)


def modify_menu():
    while True:
        menu_2()

        option = input('Choose option (1-4): ').strip()

        if option.isdigit():
            option = int(option)

            if option == 1:
                cls_term()
                title()
                modify_car()

            elif option == 2:
                cls_term()
                title()
                modify_motorcycle()

            elif option == 3:
                cls_term()
                title()
                modify_truck()

            elif option == 4:
                return

            else:
                print('-' * 80)
                input('Invalid option. Press enter to try again: ')
                cls_term()

        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()


def modify_car():
    car = Car()

    print('=' * 80)


def modify_motorcycle():
    pass


def modify_truck():
    pass