from equipment import Equipment

class Weapon(Equipment):
    def __init__(self, name, description, slot, weight, damage, value):
        super().__init__(name, description, slot, weight)
        self.damage = damage
        self.value = value

    def equip(self):
        return self
