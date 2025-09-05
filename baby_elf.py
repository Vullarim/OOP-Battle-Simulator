from enemy import Enemy

class Goblin(Enemy):
    def take_damage(self, damage):
        print("Why are you hitting a baby elf!")
        return super().take_damage(damage)