
from abc import ABC, abstractmethod


class GameItem(ABC):
    def __init__(self, item_name, weight, rarity):
        self.item_name = item_name
        self.weight = weight
        self.rarity = rarity

    @abstractmethod
    def use(self):
        pass

    def get_description(self):
        return f"{self.item_name}\n Редкость {self.rarity}\n вес {self.weight}"


class HealthPotion(GameItem):
    def use(self):
        hp = "+50 HP"
        print(f"{self.get_description()} использовано: {hp}")

    def get_description(self):
        getter = super().get_description()
        return f"{getter} - востанавливает здоровье"


class ManaCrystal(GameItem):
    def use(self):
        print(f"{self.get_description()} использовано: +30 MP")

    def get_description(self):
        getter = super().get_description()
        return f"{getter} - востанавливает ману"


n = HealthPotion("Большой флакон", 0.5, "Обычное")
n.get_description()
print(f"Зелье здоровья '{n.item_name}' (Редкость: {n.rarity}, Вес: {n.weight}) использовано: +50 HP")


m = ManaCrystal("Синий осколок", 0.3, "Редкое")
n.get_description()
print(f"Кристалл маны '{m.item_name}' (Редкость: {m.rarity}, Вес: {m.weight}) использован: +30 MP")


