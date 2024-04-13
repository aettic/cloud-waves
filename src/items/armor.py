from equipment import Equipment

class Armor(Equipment):
    def __init__(self, name, description, slot, weight, defense, value):
        super().__init__(name, description, slot, weight)
        self.name = name
        self.slot = slot
        self.defense = defense
        self.weight = weight
        self.value = value