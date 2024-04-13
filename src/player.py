class Player:
    def __init__(self, name):
        self.name = name
        self.current_zone = None
        self.score = 0
        self.inventory = []
        self.health = 100
        self.mana = 10
        self.hand = []
        self.equipment = []
        self.visited_zones = set()
        self.looked = False

    def equip(self, weapon):
        self.hand.append(weapon.equip())

    def move(self, direction):
        if direction in self.current_zone.neighbors:
            self.current_zone = self.current_zone.neighbors[direction]
        else:
            print("You cannot move in that direction.")

    def award_points(self, points):
        self.score += points

    def take_item(self, item):
        self.inventory.append(item)
        self.current_zone.remove_item(item)
        self.award_points(item.value)
        print(f"You took the {item.name}.")
