from item import Item


class Container(Item):
    def __init__(self, name, description, long_description, items):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.long_description = long_description
        self.items = items

    def __str__(self):
        return f'{self.name}: {self.description}'

    def __repr__(self):
        return f'Container({self.name}, {self.description}, {self.items})'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def get_items(self):
        return self.items

    def get_long_description(self):
        return self.long_description
