from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, baseRate, position):
        self.name = name
        self.baseRate = baseRate
        self.position = position

    @abstractmethod
    def calcu_lateSalary(self):
        pass

    def getInfo(self):
        return f"Имя: {self.name}\n  Должность: {self.position}\n Базовая ставка: {self.baseRate}"


class Manager(Employee):
    def calcu_lateSalary(self):
        return self.baseRate * 1.5

    def promote(self):
        return self.baseRate + 2000

    def work(self):
        return "Организует работу команды."


class Developer(Employee):
    def calcu_lateSalary(self):
        return self.baseRate + 500

    def promote(self):
        return self.baseRate + 5000

    def work(self):
        return "Пишет код и исправляет ошибки."


n = Manager("Иван", 7500, "Менеджер")
n.calcu_lateSalary()
m = n.work()
print(f'Сотрудник: {n.name} ({n.position}). Зарплата: {n.baseRate}. {m}')

k = Developer("Анна ", 5500, "Разработчик")
k.calcu_lateSalary()
m = k.work()
print(f'Сотрудник: {k.name} ({k.position}). Зарплата: {k.baseRate}. {m}')

