import os


def cls_term():
    os.system('cls')


def title():
    print('=' * 80)
    print('POO - VEHICLE REGISTER SYSTEM'.center(80))
    print('=' * 80)
    print()


def menu_1():
    print('=' * 80)
    print('Menu:'.center(80))
    print('=' * 80)
    print('1. Register vehicle.')
    print('2. Modify register.')
    print('3. Delete register.')
    print('4. Show registers.')
    print('5. Exit.')
    print('-' * 80)


def menu_2():
    print('=' * 80)
    print('Especify Menu:'.center(80))
    print('=' * 80)
    print('1. Car.')
    print('2. Motorcycle.')
    print('3. Truck.')
    print('4. Back.')
    print('-' * 80)


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
            print('-' * 80)
            vehicle.car_data()
        elif isinstance(vehicle, Motorcycle):
            print('=' * 80)
            print('Registered Motorcycles:')
            print('-' * 80)
            vehicle.motorcycle_data()
        elif isinstance(vehicle, Truck):
            print('=' * 80)
            print('Registered Trucks:')
            print('-' * 80)
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

        # Condicionar existência - registro carro
        if code.isdigit() and int(code) in registered_vehicles:
            car = registered_vehicles[int(code)] # Criar variável - receber registro existente
            print('=' * 80)
            print(f'You selected: {car.vehicle_data()}')
            car.modify_car() # Chamar método - modificar dados carro
            registered_vehicles[int(code)] = car # Substitui dados
            print('=' * 80)
            print('Car modified successfully.')
            break
        else:
            print('-' * 80)
            input('Car code not found. Press enter to try again: ')


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


# Criar dicionário para armazenamento
registered_vehicles = {}       


# Definir superclasse
class Vehicle:
    # Inicializar método construtor
    def __init__(self, code=0, brand='', model='', year=0, color=''):
        """_summary_

        Args:
            code (int): vehicle code. Defaults to 0.
            brand (str): vehicle brand. Defaults to ''.
            model (str): vehicle model. Defaults to ''.
            year (int): vehicle year. Defaults to 0.
            color (str): vehicle color. Defaults to ''.
        """
        # Definir atributos privados
        self._code = code
        self._brand = brand
        self._model = model
        self._year = year
        self._color = color

    # Getter
    @property
    def code(self):
        """Return private value

        Returns:
            int: vehicle code
        """
        return self._code # Retornar valor privado - código veículo

    # Setter
    @code.setter
    def code(self, value):
        """Receive value

        Args:
            value (int): vehicle code

        Raises:
            ValueError: error positive value
            ValueError: error code already registered
        """
        # Retornar erro de validação
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Register code must is a positive number.')
        if value in registered_vehicles:
            raise ValueError('This code is already in use.')
        self._code = value # Receber valor - código veículo
        registered_vehicles[value] = self # Registrar valor - dicionário de registros

    @property
    def brand(self):
        """Return private value

        Returns:
            string: vehicle brand
        """
        return self._brand # Retornar valor privado - marca veículo

    @brand.setter
    def brand(self, value):
        """Receive value

        Args:
            value (string): vehicle brand

        Raises:
            ValueError: error empty input
        """
        # Retornar erro de validação
        if not value.strip():
            raise ValueError('Brand cannot be empty.')
        self._brand = value.strip() # Receber valor - marca veículo

    @property
    def model(self):
        """Return private value

        Returns:
            string: vehicle model
        """
        return self._model # Retornar valor privado

    @model.setter
    def model(self, value):
        """Receive value

        Args:
            value (string): vehicle model

        Raises:
            ValueError: error empty input
        """
        # Retornar erro de validação
        if not value.strip():
            raise ValueError('Model cannot be empty.')
        self._model = value.strip() # Receber valor - modelo veículo

    @property
    def year(self):
        """Return private value

        Returns:
            int: vehicle year
        """
        return self._year # Retornar valor privado - modelo veículo

    @year.setter
    def year(self, value):
        """Receive value

        Args:
            value (int): vehicle year

        Raises:
            ValueError: error positive value
        """
        # Retornar erro de validação
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Year must be a positive value.')
        self._year = value # Receber valor - ano veículo

    @property
    def color(self):
        """Return private value

        Returns:
            string: vehicle color
        """
        return self._color # Retornar valor privado - cor veículo

    @color.setter
    def color(self, value):
        """Receive value

        Args:
            value (string): vehicle color

        Raises:
            ValueError: error empty input
        """
        # Retornar erro de validação
        if not value.strip():
            raise ValueError('Color cannot be empty.')
        self._color = value.strip() # Receber valor - cor veículo

    # Método - receber dados veículo
    def get_data(self):
        """Method - receive vehicle data
        """
        while True:
            try:
                self.code = int(input('Enter code: '))
                print('-' * 80)
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

        while True:
            try:
                self.brand = input('Enter brand: ')
                print('-' * 80)
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

        while True:
            try:
                self.model = input('Enter model: ')
                print('-' * 80)
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

        while True:
            try:
                self.year = int(input('Enter year manufacture (Format: YYYY): '))
                print('-' * 80)
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

        while True:
            try:
                self.color = input('Enter color: ')
                print('-' * 80)
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    # Método - modificar dados veículo
    def modify_vehicle(self):
        """Method - modify vehicle data
        """
        print('=' * 80)
        self.get_data()

    # Método - exibir dados veículo
    def vehicle_data(self):
        """Method - show vehicle data
        """
        print(f'Code: {self.code}')
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Color: {self.color}')

    # Método - criar dict veículo
    def vehicle_dict(self):
        """Create vehicle dict

        Returns:
            dict: vehicle dict
        """
        return {
            'code': self.code,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'color': self.color
        }


# Definir classe derivada - Carro
class Car(Vehicle):
    # Inicializar método construtor
    def __init__(self, code=0, brand='', model='', year=0, color='', fuel_type=''):
        """Initialize especific attributes

        Args:
            code (int): car code. Defaults to 0.
            brand (str): car brand. Defaults to ''.
            model (strl): car model. Defaults to ''.
            year (int): car year. Defaults to 0.
            color (str): car color. Defaults to ''.
            fuel_type (str): car fuel type. Defaults to ''.
        """
        super().__init__(code, brand, model, year, color) # Herdar atributos - Veículo
        self._fuel_type = fuel_type # Definir atributo privado

    @property
    def fuel_type(self):
        """Return private value

        Returns:
            string: car fuel type
        """
        return self._fuel_type # Retorna valor privado

    @fuel_type.setter
    def fuel_type(self, value):
        """Receive value

        Args:
            value (str): car fuel type

        Raises:
            ValueError: error empty input
        """
        # Retornar erro de validação
        if not value.strip():
            raise ValueError('Fuel type cannot be empty.')
        self._fuel_type = value.strip() # Receber valor - tipo de combustível carro

    # Método - receber dados carro
    def get_data(self):
        """Method - receive car data
        """
        super().get_data() # Herdar método - receber dados veículo
        while True:
            try:
                self.fuel_type = input('Enter fuel type: ')
                print('=' * 80)
                print()
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    # Método - modificar dados carro
    def modify_car(self):
        """Method - modify car data
        """
        self.get_data()

    # Método - exibir dados carro
    def car_data(self):
        """Method - show car data
        """
        super().vehicle_data() # Herdar método - exibir dados veículo
        print(f'Fuel type: {self.fuel_type}')
        print('=' * 80)
        print()

    # Método - criar dict carro
    def car_dict(self):
        """Method - create car dict

        Returns:
            dict: car dict
        """
        car_dict = super().vehicle_dict() # Herdar método - véiculo dict
        car_dict['fuel_type'] = self.fuel_type # Adicionar registro - tipo de combustível carro
        return car_dict # Retornar dict - carro