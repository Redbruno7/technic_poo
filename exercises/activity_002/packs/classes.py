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
        while True:
            try:
                new_code = input(f'Enter code [{self.code}]: ').strip() # Criar nova variável e mostrar valor atual

                # Condicionar existência - código veículo
                if new_code:
                    self.code = int(new_code) # Receber novo valor - código veículo
                print('-' * 80)
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

        while True:
            try:
                new_brand = input(f'Enter brand [{self.brand}]: ').strip() # Criar nova variável e mostrar valor atual

                # Condicionar existência - marca veículo
                if new_brand:
                    self.brand = new_brand # Receber novo valor - marca veículo
                print('-' * 80)
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

        while True:
            try:
                new_model = input(f'Enter model [{self.model}]: ').strip() # Criar nova variável e mostrar valor atual

                # Condicionar existência - modelo veículo
                if new_model:
                    self.model = new_model # Receber novo valor - modelo veículo
                print('-' * 80)
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)
    
        while True:
            try:
                new_year = input(
                    f'Enter year manufacture [{self.year}]: ').strip() # Criar nova variável e mostrar valor atual

                # Condicionar existência - ano veículo
                if new_year:
                    self.year = int(new_year) # Receber novo valor - ano veículo
                    print('-' * 80)
                    break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

        while True:
            try:
                new_color = input(f'Enter color [{self.color}]: ').strip() # Criar nova variável e mostrar valor atual

                # Condicionar existência - cor veículo
                if new_color:
                    self.color = new_color # Receber novo valor - cor veículo
                    print('-' * 80)
                    break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    # Método - exibir dados veículo
    def vehicle_data(self):
        """Method - show vehicle data
        """
        print('-' * 80)
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
        super().modify_vehicle() # Herdar método - modificar dados veículo
        while True:
            try:
                new_fuel_type = input(f'Enter fuel type [{self.fuel_type}]: ').strip() # Criar nova variável e mostrar valor atual
                if new_fuel_type:
                    self.fuel_type = new_fuel_type # Receber novo valor - tipo de combustível carro
                print('=' * 80)
                print()
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

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

# Definir classe derivada - motocicleta
class Motorcycle(Vehicle):
    # Inicializar método construtor
    def __init__(self, code=0, brand='', model='', year=0, color='', motorcycle_type=''):
        """Initialize especific attribute

        Args:
            code (int): motorcycle code. Defaults to 0.
            brand (str): motorcycle brand. Defaults to ''.
            model (str): motorcycle model. Defaults to ''.
            year (int): motorcycle year. Defaults to 0.
            color (str): motorcycle color. Defaults to ''.
            motorcycle_type (str): motorcycle type. Defaults to ''.
        """
        super().__init__(code, brand, model, year, color) # Herdar atributos - Veículo
        self._motorcycle_type = motorcycle_type # Definir atributo privado

    @property
    def motorcycle_type(self):
        """Return private value

        Returns:
            str: motorcycle type
        """
        return self._motorcycle_type # Retornar valor privado

    @motorcycle_type.setter
    def motorcycle_type(self, value):
        """Receive value

        Args:
            value (str): motorcycle type

        Raises:
            ValueError: errpr empty input
        """
        # Condicionar existência
        if not value.strip():
            raise ValueError('Motorcycle type cannot be empty.')
        self._motorcycle_type = value.strip() # Receber valor - tipo de motocicleta

    # Método - receber dados motocicleta
    def get_data(self):
        """Method - receive motorcycle data
        """
        super().get_data() # Herdar método - receber dados veículo
        while True:
            try:
                self._motorcycle_type = input('Enter motorcycle type: ')
                print('=' * 80)
                print()
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    # Método - modificar dados motocicleta
    def modify_motorcycle(self):
        """Method - modify motorcycle data
        """
        super().modify_vehicle() # Herdar método - modificar veículo
        while True:
            try:
                new_motorcycle_type = input(f'Enter motorcycle type [{self.motorcycle_type}]: ').strip() # Criar nova variável e mostrar valor atual
                if new_motorcycle_type:
                    self.motorcycle_type = new_motorcycle_type # Receber novo valor - tipo de motocicleta
                print('=' * 80)
                print()
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    # Método - exibir dados motocicleta
    def motorcycle_data(self):
        """Method - show motorcycle data
        """
        super().vehicle_data() # Herdar método - exibir dados veículo
        print(f'Motorcycle type: {self._motorcycle_type}')
        print('=' * 80)
        print()

    # Método - criar dict motocicleta
    def motorcycle_dict(self):
        """Method - create motorcycle dict

        Returns:
            dict: motorcycle dict
        """
        motorcycle_dict = super().vehicle_dict() # Herdar método - dict veículo
        motorcycle_dict['motorcycle_type'] = self.motorcycle_type # Adicionar registro - tipo de motocicleta
        return motorcycle_dict # Retornar dict - motocicleta


# Definir classe derivada - caminhão
class Truck(Vehicle):
    # Inicializar método construtor
    def __init__(self, code=0, brand='', model='', year=0, color='', load_capacity=0):
        """Initialize especific attribute

        Args:
            code (int): truck code. Defaults to 0.
            brand (str): truck brand. Defaults to ''.
            model (str): truck model. Defaults to ''.
            year (int): truck year. Defaults to 0.
            color (str): truck color. Defaults to ''.
            load_capacity (int, float): truck load capacity. Defaults to 0.
        """
        super().__init__(code, brand, model, year, color) # Herdar atributos - Veículo
        self._load_capacity = load_capacity # Definir atributo privado

    @property
    def load_capacity(self):
        """Return private value

        Returns:
            int, float: truck load capacity
        """
        return self._load_capacity # Retornar valor privado

    @load_capacity.setter
    def load_capacity(self, value):
        """Receive value

        Args:
            value (int, float): truck load capacity

        Raises:
            ValueError: error positive value
        """
        # Condicionar existência
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError('Load capacity must be a positive value.')
        self._load_capacity = value # Receber valor - capacidade de carga caminhão

    # Método - receber dados caminhão
    def get_data(self):
        """Method - receive truck data
        """
        super().get_data() # Herdar método - receber dados veículo
        while True:
            try:
                self._load_capacity = float(input('Enter load capacity: '))
                print('=' * 80)
                print()
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    # Método - modificar dados caminhão
    def modify_truck(self):
        """Method - modify truck data
        """
        super().modify_vehicle() # Herdar método - modificar dados caminhão
        while True:
            try:
                new_load_capacity = input(f'Enter load capacity [{self.load_capacity}]: ').strip() # Criar nova variável e mostrar valor atual
                if new_load_capacity:
                    self.fuel_type = new_load_capacity # Receber novo valor - capacidade de carga caminhão
                print('=' * 80)
                print()
                break
            except ValueError as e:
                print('-' * 80)
                print(e)
                print('-' * 80)

    # Método - exibir dados caminhão
    def truck_data(self):
        """Method - show truck data
        """
        super().vehicle_data() # Herdar método - exibir dados veículo
        print(f'Load capacity: {self._load_capacity:.2f} kg')
        print('=' * 80)
        print()

    # Método - criar dict caminhão
    def truck_dict(self):
        """Method - create truck dict

        Returns:
            dict: truck dict
        """
        truck_dict = super().vehicle_dict() # Herdar método - dict veículo
        truck_dict['load_capacity'] = self.load_capacity # Adicionar registro - capacidade de carga caminhão
        return truck_dict # Retornar dict - caminhão