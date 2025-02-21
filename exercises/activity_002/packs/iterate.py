from packs.menu import cls_term, title, menu_1, menu_2
from packs.classes import Car, Motorcycle, Truck, registered_vehicles


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
                modify_menu()
            elif option == 3:
                pass
            elif option == 4:
                cls_term()
                title()
                list_registered_vehicles()
                input('Press enter to continue: ')
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


def list_registered_vehicles():
    if registered_vehicles:
        print('=' * 80)
        print('Registered Vehicles:')
        for vehiccle in registered_vehicles.values():
            vehiccle.vehicle_data()
        print('=' * 80)
    else:
        print('=' * 80)
        print('No vehicles registered yet.')
        print('=' * 80)


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
            return main_menu()
        elif register_again == 'y':
            cls_term()
            title()
            return register_menu()
        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            print('-' * 80)


def modify_menu():
    cls_term()
    title()
    menu_2()
    option = input('Choose option (1-4): ').strip()

    if option.isdigit():
        option = int(option)

        if option == 1:
            modify_car()
            print()
            modify_again()
        elif option == 2:
            modify_motorcycle()
            print()
            modify_again()
        elif option == 3:
            modify_truck()
            print()
            modify_again()
        elif option == 4:
            return main_menu()
        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()

    else:
        print('-' * 80)
        input('Invalid option. Press enter to try again: ')
        cls_term()


def modify_car():
    while True:
        cls_term()
        title()
        print('Modify Car Information:')
        print('=' * 80)

        # Exibe todos os carros registrados
        for vehicle in registered_vehicles.values():
            if isinstance(vehicle, Car):
                vehicle.vehicle_data()

        print('=' * 80)
        code = input('Enter car code to modify: ').strip()
        print('-' * 80)

        if code.isdigit() and int(code) in registered_vehicles:
            car = registered_vehicles[int(code)]

            print(f'You selected: {car.vehicle_data()}')
            car.get_data() # Chama o método de modificação de dados
            break
        else:
            print('-' * 80)
            input('Car code not found. Press enter to try again: ')


def modify_motorcycle():
    while True:
        cls_term()
        title()
        print('Modify Motorcycle Information:')
        print('=' * 80)

        # Exibe todos as Motocicletas registradas
        for vehicle in registered_vehicles.values():
            if isinstance(vehicle, Motorcycle):
                vehicle.vehicle_data()

        print('=' * 80)
        code = input('Enter mortorcycle code to modify: ').strip()
        print('-' * 80)

        if code.isdigit() and int(code) in registered_vehicles:
            motorcycle = registered_vehicles[int(code)]

            print(f'You selected: {motorcycle.vehicle_data()}')
            motorcycle.get_data() # Chama o método de modificação de dados
            break
        else:
            print('-' * 80)
            input('Motorcycle code not found. Press enter to try again: ')


def modify_truck():
    while True:
        cls_term()
        title()
        print('Modify Truck Information:')
        print('=' * 80)

        # Exibe todos os carros registrados
        for vehicle in registered_vehicles.values():
            if isinstance(vehicle, Truck):
                vehicle.vehicle_data()

        print('=' * 80)
        code = input('Enter car code to modify: ').strip()
        print('-' * 80)

        if code.isdigit() and int(code) in registered_vehicles:
            truck = registered_vehicles[int(code)]

            print(f'You selected: {truck.vehicle_data()}')
            truck.get_data() # Chama o método de modificação de dados
            break
        else:
            print('-' * 80)
            input('Truck code not found. Press enter to try again: ')


def modify_again():
    print('=' * 80)
    while True:
        modify_again = input(
            'Continue modify (y/n): '
        ).strip().lower()

        if modify_again == 'n':
            return main_menu()
        elif modify_again == 'y':
            cls_term()
            title()
            return modify_menu()
        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            print('-' * 80)