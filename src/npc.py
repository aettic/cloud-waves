class NPC:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return f'{self.name} has {self.hp} hp and {self.damage} damage'

    def take_damage(self, damage):
        self.hp -= damage

    def attack(self, enemy):
        enemy.take_damage(self.damage)