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
        return True

    def move(self, direction=None):
        if direction is None:
            direction = input("Which direction would you like to move? ")
        if direction in self.current_zone.neighbors:
            self.current_zone = self.current_zone.neighbors[direction]
        else:
            print("You cannot move in that direction.")
        return True

    def look(self):
        print(self.current_zone.get_long_description())
        self.looked = True
        return True

    def award_points(self, points):
        self.score += points

    def take_item(self, item_name=None):
        if self.current_zone.items:
            if item_name is None:
                item_name = input("What would you like to take? ")

            for item in self.current_zone.items:
                if item.name.lower() == item_name.lower():
                    self.inventory.append(item)
                    self.current_zone.remove_item(item)
                    self.award_points(item.value)
                    print(f"You took the {item.name}.")
                    break
                else:
                    print("That item is not here.")
        else:
            print(f"There is no {item_name} here.")
        return True

    def use_item_from_inventory(self, item_name=None):
        if item_name is None:
            item_name = input("Which item would you like to use? ")
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use_item()
                if item.is_expendable:
                    item.quantity -= 1
                    if item.quantity < 1:
                        self.inventory.remove(item)
                        # replace with an item-specific "expend" string for when quantity hits 0
                        print(f"You have used up the {item.name}.")
                return True
        print("You do not have that item.")
        return True


    def open_inventory(self):
        if len(self.inventory) < 1:
            print("Your inventory is empty.")
        else:
            print("You have the following items in your inventory:")
            for item in self.inventory:
                print(item)
        return True