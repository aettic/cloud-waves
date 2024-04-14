from item import Item


class Equipment(Item):
    def __init__(self, name, description, slot, weight, value, long_description, use):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.slot = slot
        self.weight = weight
        self.value = value
        self.long_description = long_description
        self.use = use
