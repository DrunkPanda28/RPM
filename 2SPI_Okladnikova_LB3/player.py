class Player:
    def __init__(self, name):
        self._name = name
        self._health = 100  # Начальное здоровье
        self._level = 1     # Начальный уровень
        self._experience = 0  # Начальный опыт

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        # Здоровье не может превышать 100 и быть меньше 0
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        # Уровень не должен быть ниже 1
        if value < 1:
            self._level = 1
        else:
            self._level = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        # Опыт не должен быть ниже 1
        if value < 0:
            self._experience = 0
        else:
            self._experience = value
            # Проверяем уровень в методе check_level_up
            self.check_level_up()

    # Увеличиваем опыт на указанное кол-во
    def gain_experience(self, amount):
        self.experience += amount

    # Проверка на достижения необходиого кол-ва опыта для повышения уровня
    def check_level_up(self):
        if self._experience >= 100:  # Уровень увеличивается каждые 100 очков опыта
            self._level += 1
            self._experience -= 100  # Сбрасываем опыт для след уровня
            print(f"{self.name} поднялся на уровень! Теперь уровень: {self.level}")

    def __str__(self):
        return f"Игрок: {self.name}, Здоровье: {self.health}, Уровень: {self.level}, Опыт: {self.experience}"


player = Player("Алекс")
print(player)  # Игрок: Алекс, Здоровье: 100, Уровень: 1, Опыт: 0

player.gain_experience(150)
print(player)  # Теперь уровень 2
