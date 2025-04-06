class Device:
    def __init__(self, power=100):
        self.power = power

    def turn_on(self):
        print("Устройство включено.")


class NetworkedDevice(Device):
    def __init__(self, power, ip_address="192.168.1.1"):
        super().__init__(power)
        self.ip_address = ip_address

    def connect(self):
        print(f"Подключение к сети по адресу {self.ip_address}")


class PortableDevice(Device):
    def __init__(self, power, battery_level=100):
        Device.__init__(self, power)
        self.battery_level = battery_level

    def charge(self):
        print("Зарядка устройства.")


class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        super().__init__(power, ip_address)
        super().__init__(battery_level)

    def call(self):
        print("Делаю звонок...")


smartphone = Device(100)

smart = SmartPhone(100, "192.168.1.1", 100)
# Включаем смартфон
smartphone.turn_on()

# Подключаемся к сети
smart.connect()

# Заряжаем устройство


# Звоним
smart.call()


