from packs.print import cls_term, title
from packs.classes import Vehicle, Car, Motorcycle, Truck


def menu():
    while True:
        cls_term()
        title()
        print('=' * 80)
        print('Menu:'.center(80))
        print('=' * 80)
        print('1. Register vehicle.')
        print('2. Modify register.')
        print('3. Delete register.')
        print('4. Show registers.')
        print('5. Exit.')
        print('-' * 80)

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


def especify_menu():
    print('=' * 80)
    print('Especify Menu:'.center(80))
    print('=' * 80)
    print('1. Car.')
    print('2. Motorcycle.')
    print('3. Truck.')
    print('4. Back.')
    print('-' * 80)


def register_menu():
    while True:
        especify_menu()
        option = input('Choose option (1-4): ').strip()

        if option.isdigit():
            option = int(option)

            if option == 1:
                while True:
                    cls_term()
                    title()
                    print('=' * 80)

                    car_data = register_car()

                    print('=' * 80)
                    print('Car registered successfully.')
                    print('-' * 80)

                    for key, value in car_data.items():
                        print(f'{key}: {value}')

                    print('=' * 80)
                    print()
                    register_again()

            elif option == 2:
                while True:
                    cls_term()
                    title()
                    print('=' * 80)

                    motorcycle_data = register_motorcycle()

                    print('=' * 80)
                    print('Motorcycle registered successfully.')
                    print('-' * 80)

                    for key, value in motorcycle_data.items():
                        print(f'{key}: {value}')

                    print('=' * 80)
                    print()
                    register_again()

            elif option == 3:
                while True:
                    cls_term()
                    title()
                    print('=' * 80)

                    truck_data = register_truck()

                    print('=' * 80)
                    print('Truck registered successfully.')
                    print('-' * 80)

                    for key, value in truck_data.items():
                        print(f'{key}: {value}')
                    print('=' * 80)
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
    while True:
        try:
            car.get_data()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)
    return car.car_dict()


def register_motorcycle():
    motorcycle = Motorcycle()
    while True:
        try:
            motorcycle.get_data()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)
    return motorcycle.motorcycle_dict()


def register_truck():
    truck = Truck()
    while True:
        try:
            truck.get_data()
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)
    return truck.truck_dict()


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
