from enemy import Enemy
import random

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = random.randint(75, 100)
        self.health = 200
    def attack(self, target):
        if random.randint(1,5) == 5:
            print(f"{target.name} was stunned by {self.name}")
            target.isStunned = True
        return random.randint(50, self.attack_power)