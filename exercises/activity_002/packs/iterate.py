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

            if option in [1, 2, 3, 4]:
                cls_term()
                print('=' * 80)
                print()
                especify_menu()
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
    while True:
        print('=' * 80)
        print('Especify Menu:'.center(80))
        print('=' * 80)
        print('1. Car.')
        print('2. Motorcycle.')
        print('3. Truck.')
        print('4. Back.')
        print('-' * 80)

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
                    print(car_data)
                    print('=' * 80)
                    print()

                    print('=' * 80)
                    try_again = input(
                        'Continue register (y/n): '
                    ).strip().lower()

                    if try_again == 'n':
                        return
                    elif try_again != 'y':
                        print('-' * 80)
                        input('Invalid option. Press enter to try again: ')

            elif option == 2:
                pass
            elif option == 3:
                pass
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