from item import Item


class Equipment(Item):
    def __init__(self, name, description, slot, weight):
        super().__init__(name, description)
        self.slot = slot
        self.weight = weight
