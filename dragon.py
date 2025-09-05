from enemy import Enemy
import random

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = random.randint(75, 100)
        self.health = 250
    def attack(self):
        return random.randint(50, self.attack_power)