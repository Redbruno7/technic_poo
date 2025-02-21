from packs.menu import cls_term, title, menu_1, menu_2
from packs.classes import Car, Motorcycle, Truck, registered_vehicles

# Menu Principal
def main_menu():
    """Function - main menu to call others menus
    """
    while True:
        cls_term()
        title()
        menu_1()

        option = input('Choose option (1-5): ')

        # Validar opção
        if option.isdigit():
            option = int(option)

            if option == 1:
                # Invocar funções
                cls_term()
                title()
                register_menu() # Chamar função registro
            elif option == 2:
                cls_term()
                title()
                modify_menu() # Chamar função modificar
            elif option == 3:
                cls_term()
                title()
                del_menu() # Chamar função deletar
            elif option == 4:
                cls_term()
                title()
                list_registered_vehicles() # Chamar função de exibição
                print('=' * 80)
                input('Press enter to continue: ')
            elif option == 5:
                print('=' * 80)
                print()
                print('=' * 80)
                print('Shutting down system.')
                print('=' * 80)
                print()
                break # Encerrar o sistema
            else:
                print('-' * 80)
                input('Invalid option. Press enter to try again: ')
                cls_term()

        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()

# Exibir registros de veículos
def list_registered_vehicles():
    """Function - show registers vehicles
    """
    # Condicionar de existência
    if registered_vehicles:
        print('=' * 80)
        print('Registered Vehicles:'. center(80))
        print('=' * 80)
        print()

    for vehicle in registered_vehicles.values():
        if isinstance(vehicle, Car):
            print('=' * 80)
            print('Registered Cars:')
            vehicle.car_data()
        elif isinstance(vehicle, Motorcycle):
            print('=' * 80)
            print('Registered Motorcycles:')
            vehicle.motorcycle_data()
        elif isinstance(vehicle, Truck):
            print('=' * 80)
            print('Registered Trucks:')
            vehicle.truck_data()
        else:
            vehicle.vehicle_data()

# Registrar
def register_menu():
    """Function - register menu

    Returns:
        main menu: return to main menu
    """
    while True:
        menu_2()

        option = input('Choose option (1-4): ').strip()

        if option.isdigit():
            option = int(option)

            if option == 1:
                while True:
                    cls_term()
                    title()
                    register_car() # Chamar função - registrar carro
                    print()
                    register_again() # Iterar para registrar novamente

            elif option == 2:
                while True:
                    cls_term()
                    title()
                    register_motorcycle() # Chamar função - registrar motocicleta
                    print()
                    register_again()

            elif option == 3:
                while True:
                    cls_term()
                    title()
                    register_truck() # Chamar função - registrar caminhão
                    print()
                    register_again()

            elif option == 4:
                return # Retornar ao menu principal

            else:
                print('-' * 80)
                input('Invalid option. Press enter to try again: ')
                cls_term()

        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()


def register_car():
    """Register car function

    Returns:
        method: return method car get data
    """
    car = Car() # Instanciar objeto - carro

    print('=' * 80)
    while True:
        try:
            car.get_data() # Chamar método - receber dados carro
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('=' * 80)
    print('Car registered successfully.')
    return car.car_data() # Retornar método - dados carro


def register_motorcycle():
    """Function - register motorcycle

    Returns:
        method: return method motorcycle get data
    """
    motorcycle = Motorcycle() # Instanciar objeto - motocicleta

    print('=' * 80)
    while True:
        try:
            motorcycle.get_data() # Chamar método - receber dados motocicleta
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('=' * 80)
    print('Motorcycle registered successfully.')
    return motorcycle.motorcycle_data() # Retornar método - dados motocicleta


def register_truck():
    """Function - register truck

    Returns:
        method: return method truck get data
    """
    truck = Truck() # Instanciar objeto - caminhão

    print('=' * 80)
    while True:
        try:
            truck.get_data() # Chamar método - receber dados caminhão
            break
        except ValueError as e:
            print('-' * 80)
            print(e)
            print('-' * 80)

    print('=' * 80)
    print('Truck registered successfully.')
    return truck.truck_data() # Retornar método - dados caminhão


def register_again():
    """Function - continue registering

    Returns:
        main menu: return to main menu
        register menu: return to register menu
    """
    print('=' * 80)
    while True:
        register_again = input(
            'Continue register (y/n): '
        ).strip().lower()

        # Validar entrada
        if register_again == 'n':
            return main_menu() # Retornar para o Menu Principal
        elif register_again == 'y':
            cls_term()
            title()
            return register_menu() # Retornar para o Menu Registro
        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            print('-' * 80)

# Modificar
def modify_menu():
    """Function - modify menu

    Returns:
        main menu: return to main menu
    """
    cls_term()
    title()
    menu_2()
    option = input('Choose option (1-4): ').strip()

    # Validar opção
    if option.isdigit():
        option = int(option)

        if option == 1:
            modify_car() # Chamar função - modificar carro
            print()
            modify_again() # Chamar função - modificar novamente
        elif option == 2:
            modify_motorcycle() # Chamar função - modificar motocicleta
            print()
            modify_again()
        elif option == 3:
            modify_truck() # Chamar função - modificar caminhão
            print()
            modify_again()
        elif option == 4:
            return main_menu() # Retornar ao menu principal
        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()

    else:
        print('-' * 80)
        input('Invalid option. Press enter to try again: ')
        cls_term()


def modify_car():
    """Function - modify car data
    """
    while True:
        cls_term()
        title()
        print('=' * 80)
        print('Modify Car Information:')
        print('=' * 80)
        print()

        # Exibir todos os carros registrados
        for vehicle in registered_vehicles.values():

            # Condicionar existência - carro 
            if isinstance(vehicle, Car):
                print('=' * 80)
                print('Registered Cars:')
                vehicle.vehicle_data() # Exibir dados - carro
                print('=' * 80)
                print()

        print('=' * 80)
        code = input('Enter car code to modify: ').strip()
        print('=' * 80)

        # Condicionar existência - registro carro
        if code.isdigit() and int(code) in registered_vehicles:
            car = registered_vehicles[int(code)] # Criar variável - receber registro existente

            print(f'You selected: {car.vehicle_data()}')
            car.modify_car() # Chamar método - modificar dados carro
            registered_vehicles[int(code)] = car # Substitui dados
            print('-' * 80)
            print('Car modified successfully.')
            break
        else:
            print('-' * 80)
            input('Car code not found. Press enter to try again: ')


def modify_motorcycle():
    """Function - modify motorcycle data
    """
    while True:
        cls_term()
        title()
        print('Modify Motorcycle Information:')
        print('=' * 80)
        print()

        # Exibe todos as motocicletas registradas
        for vehicle in registered_vehicles.values():

            # Condicionar existência - motocicleta
            if isinstance(vehicle, Motorcycle):
                print('=' * 80)
                print('Registered Motorcycles:')
                vehicle.vehicle_data() # Exibir dados - motocicleta
                print('=' * 80)
                print()

        print('=' * 80)
        code = input('Enter mortorcycle code to modify: ').strip()
        print('-' * 80)

        # Condicionar existência - registro motocicleta
        if code.isdigit() and int(code) in registered_vehicles:
            motorcycle = registered_vehicles[int(code)] # Criar variável - receber registro existente

            print(f'You selected: {motorcycle.vehicle_data()}')
            motorcycle.modify_motorcycle() # Chamar método - modificar dados motocicleta
            registered_vehicles[int(code)] = motorcycle # Substitui dados
            print('-' * 80)
            print('Motorcycle modified successfully.')
            break
        else:
            print('-' * 80)
            input('Motorcycle code not found. Press enter to try again: ')


def modify_truck():
    """Function - modify truck data
    """
    while True:
        cls_term()
        title()
        print('Modify Truck Information:')
        print('=' * 80)
        print()

        # Exibe todos os caminhões registrados
        for vehicle in registered_vehicles.values():

            # Condicionar existência - caminhão
            if isinstance(vehicle, Truck):
                print('=' * 80)
                print('Registered Trucks:')
                vehicle.vehicle_data() # Exibir dados - caminhão
                print('=' * 80)
                print()

        print('=' * 80)
        code = input('Enter car code to modify: ').strip()
        print('-' * 80)

        # Condicionar existência - registro caminhão
        if code.isdigit() and int(code) in registered_vehicles:
            truck = registered_vehicles[int(code)] # Criar variável - receber registro existente

            print(f'You selected: {truck.vehicle_data()}')
            truck.modify_truck() # Chamar método - modificar dados caminhão
            registered_vehicles[int(code)] = truck # Substitui dados
            print('-' * 80)
            print('Truck modified successfully.')
            break
        else:
            print('-' * 80)
            input('Truck code not found. Press enter to try again: ')


def modify_again():
    """Function - continue modifying

    Returns:
        main menu: return to main menu
        modify menu: return to modify menu
    """
    print('=' * 80)
    while True:
        modify_again = input(
            'Continue modify (y/n): '
        ).strip().lower()

        # Validar entrada
        if modify_again == 'n':
            return main_menu() # Retornar ao menu principal
        elif modify_again == 'y':
            cls_term()
            title()
            return modify_menu() # Retornar ao menu modificar
        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            print('-' * 80)

# Deletar
def del_menu():
    """Function - delete menu

    Returns:
        main menu: return to main menu
    """
    cls_term()
    title()
    menu_2()
    option = input('Choose option (1-4): ').strip()

    # Validar opção
    if option.isdigit():
        option = int(option)

        if option == 1:
            del_car() # Chamar função - deletar carro
        elif option == 2:
            del_motorcycle() # Chamar função - deletar motocicleta
        elif option == 3:
            del_truck() # Chamar função - deletar caminhão
        elif option == 4:
            return main_menu() # Retornar ao menu principal
        else:
            print('-' * 80)
            input('Invalid option. Press enter to try again: ')
            cls_term()

    else:
        print('-' * 80)
        input('Invalid option. Press enter to try again: ')
        cls_term()


def del_car():
    """Function - delete car data
    """
    while True:
        cls_term()
        title()
        print('Delete Car Register:')
        print('=' * 80)

        # Exibir todos os carros registrados
        for vehicle in registered_vehicles.values():

            # Condicionar existência - carro 
            if isinstance(vehicle, Car):
                vehicle.vehicle_data() # Exibir dados - carro

        print('=' * 80)
        code = input('Enter car code to delete: ').strip()
        print('-' * 80)

        # Condicionar existência - registro carro
        if code.isdigit() and int(code) in registered_vehicles:
            del_car = registered_vehicles.pop(int(code)) # Remover carro
            print(f'Car (Code: {del_car.code}) deleted successfully.')
            break
        else:
            print('-' * 80)
            input('Car code not found. Press enter to try again: ')


def del_motorcycle():
    """Function - delete motorcycle data
    """
    while True:
        cls_term()
        title()
        print('Delete Motorcycle Register:')
        print('=' * 80)

        # Exibir todas as motocicletas registradas
        for vehicle in registered_vehicles.values():

            # Condicionar existência - motocicleta 
            if isinstance(vehicle, Motorcycle):
                vehicle.vehicle_data() # Exibir dados - motocicleta

        print('=' * 80)
        code = input('Enter motorcycle code to delete: ').strip()
        print('-' * 80)

        # Condicionar existência - registro motocicleta
        if code.isdigit() and int(code) in registered_vehicles:
            del_motorcycle = registered_vehicles.pop(int(code)) # Remover motocicleta
            print(f'Motorcycle (Code: {del_motorcycle.code}) deleted successfully.')
            break
        else:
            print('-' * 80)
            input('Motorcycle code not found. Press enter to try again: ')


def del_truck():
    """Function - delete truck data
    """
    while True:
        cls_term()
        title()
        print('Delete Truck Register:')
        print('=' * 80)

        # Exibir todos os caminhões registrados
        for vehicle in registered_vehicles.values():

            # Condicionar existência - caminhão 
            if isinstance(vehicle, Truck):
                vehicle.vehicle_data() # Exibir dados - caminhão

        print('=' * 80)
        code = input('Enter truck code to delete: ').strip()
        print('-' * 80)

        # Condicionar existência - registro caminhão
        if code.isdigit() and int(code) in registered_vehicles:
            del_truck = registered_vehicles.pop(int(code)) # Remover caminhão
            print(f'Truck (Code: {del_truck.code}) deleted successfully.')
            break
        else:
            print('-' * 80)
            input('Truck code not found. Press enter to try again: ')