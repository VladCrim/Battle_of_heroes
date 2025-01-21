class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            print(f"{self.player.name} атаковал {self.computer.name} и нанес {self.player.attack_power} урона. "
                  f"У {self.computer.name} осталось {self.computer.health} здоровья.")

            if not self.computer.is_alive():
                break  # Если компьютер умер, игра заканчивается

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"{self.computer.name} атаковал {self.player.name} и нанес {self.computer.attack_power} урона. "
                  f"У {self.player.name} осталось {self.player.health} здоровья.")

        # Определение победителя
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Создание героев
player = Hero("Игрок")
computer = Hero("Компьютер")

# Создание и запуск игры
game = Game(player, computer)
game.start()



