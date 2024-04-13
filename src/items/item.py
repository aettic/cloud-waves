class Item:
    def __init__(self, item_id, name, description, value, long_description, use):
        self.id = item_id
        self.name = name
        self.description = description
        self.value = value
        self.long_description = long_description
        self.use = use

    def __str__(self):
        return f'{self.name}: {self.long_description}. It is worth {self.value} gold. You can use it to {self.use}.'

    def __repr__(self):
        return f'Item({self.id}, {self.name}, {self.description}, {self.value}, {self.long_description}, {self.use})'

