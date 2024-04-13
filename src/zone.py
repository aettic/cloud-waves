class Zone:
    def __init__(self, zone_id, name, description, long_description):
        self.id = zone_id
        self.name = name
        self.description = description
        self.long_description = long_description
        self.items = []
        self.neighbors = {}
        self.npcs = []

    def add_neighbor(self, neighbor, direction):
        self.neighbors[direction] = neighbor

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_long_description(self):
        return self.long_description
