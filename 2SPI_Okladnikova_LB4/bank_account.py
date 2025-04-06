from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, Owner, AccountNumber):
        self.Balance = 0
        self.Owner = Owner
        self.AccountNumber = AccountNumber

    @abstractmethod
    def calcu_lateInterest(self):
        pass

    def deposit(self, amount):
        if amount > 0:
            self.Balance += amount
        return self.Balance

    def withdraw(self, amount):
        if self.Balance > amount:
            self.Balance -= amount
        else:
            return f"Недостаточно средств. \n Ваш баланс: {self.Balance}"
        return f'Ваш баланс: {self.Balance}'

    def __str__(self):
        print(f"Счет {self.AccountNumber} (Владелец: {self.Owner}). Баланс: {self.Balance}. Проценты: {amount}")


class SavingsAccount(BankAccount):
    def calcu_lateInterest(self):
        return self.Balance * 0.5


class CheckingAccount(BankAccount):
    def calcu_lateInterest(self):
        return 0


sav = SavingsAccount("Joh", "2139")
sav.deposit(1333)
savInterest = sav.calcu_lateInterest()
print(f"Счет {sav.AccountNumber} (Владелец: {sav.Owner}). Баланс: {sav.Balance}. Проценты: {savInterest}")

cheking = CheckingAccount("jon", "21313")
cheki_interest = cheking.calcu_lateInterest()
print(f"Счет {cheking.AccountNumber} (Владелец: {cheking.Owner}). Баланс: {cheking.Balance}. Проценты: {cheki_interest}")


