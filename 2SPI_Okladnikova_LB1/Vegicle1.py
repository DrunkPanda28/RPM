class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    def start_engine(self):
        return "Двигатель запущен"


class WheeledVehicle(Vehicle):
    def __init__(self, wheel_count, max_speed, fuel_type):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.wheel_count = wheel_count

    def check_tires(self):
        return f"Проверка {self.wheel_count} колес"


class CargoTransport(Vehicle):
    def __init__(self, cargo_capacity, max_speed, fuel_type):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0

    # проверка на свободное место в грузовике
    def load_cargo(self, maximum_cargo):
        if self.current_cargo + maximum_cargo <= self.cargo_capacity:
            self.current_cargo += maximum_cargo
            return f"Загружено {maximum_cargo} кг. Текущий груз: {self.current_cargo} кг."
        else:
            return "Недостаточно места для груза"


class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity
        self.current_passengers = 0

    def board_passengers(self, passenger):
        if self.current_passengers + passenger <= self.passenger_capacity:
            self.current_passengers += passenger
            return f"Посадка {passenger} пассажиров. Текущие пассажиры: {self.current_passengers}."
        else:
            return "Недостаточно места для пассажиров"


class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, wheel_count, cargo_capacity, max_weight, max_speed, fuel_type):
        WheeledVehicle.__init__(self, wheel_count, max_speed, fuel_type)
        CargoTransport.__init__(self, max_speed, fuel_type, cargo_capacity)
        self.max_weight = max_weight

    def reinforce_frame(self):
        if self.max_weight > self.cargo_capacity:
            return "Груз слишком тяжелый"
        else:
            return f"Максимальный груз: {self.max_weight}"


class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level):
        super().__init__(max_speed, fuel_type)
        self.emission_level = emission_level

    def reduce_emission(self):
        self.emission_level -= 1
        return f"Уровень выбросов снижен. Текущий уровень: {self.emission_level}"


class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, wheel_count, cargo_capacity, max_weight, max_speed, fuel_type, passenger_capacity, emission_level):
        HeavyDutyVehicle.__init__(self, wheel_count, cargo_capacity, max_weight, max_speed, fuel_type)
        PassengerTransport.__init__(self,  max_speed, fuel_type, passenger_capacity)
        EcoFriendlyVehicle.__init__(self, fuel_type, max_speed, emission_level)

    def status(self):
        return (f"Скорость: {self.max_speed} км/ч, "
                f"Топливо: {self.fuel_type}, "
                f"Груз: {self.current_cargo}/{self.cargo_capacity} кг, "
                f"Пассажиры: {self.current_passengers}/{self.passenger_capacity}, "
                f"Выбросы: {self.emission_level}")


van = HybridDeliveryVan(max_speed=120, fuel_type="дизель", wheel_count=4, cargo_capacity=2000, max_weight=3000,
                        passenger_capacity=8, emission_level=5)


print(van.start_engine())
print(van.check_tires())
print(van.load_cargo(500))
print(van.board_passengers(4))
print(van.reduce_emission())
print(van.reinforce_frame())
print(van.status())

