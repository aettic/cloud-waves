import json
from player import Player
from items.item import Item
from zone import Zone


# introductory functions

def welcome():
    name = input("Welcome, what's your name name: ")
    return Player(name)


def story():
    print("You have entered a well-built cabin, in the hopes of finding the ancient amulet.")


# administrative functions

def print_help():
    print("Commands:")
    print("  move (m) - Move to a different zone.")
    print("  look (l) - Look around.")
    print("  quit (q) - Quit the game.")
    print("  help (?) - Print this list of commands.")


def print_instructions(player):
    if player.current_zone not in player.visited_zones:
        player.visited_zones.add(player.current_zone)
        print(f"\nYou are in the {player.current_zone.name}, {player.current_zone.description}.")
    else:
        print(f"\nYou are in the {player.current_zone.name}.")

    if player.looked:
        if player.current_zone.items:
            print("You see the following items:")
            for item in player.current_zone.items:
                print(f"  {item.name}")

    player.looked = False


def goodbye(player):
    print(f"Goodbye, {player.name}!")
    print(f"Your score was {player.score}.")


# data loading functions

def load_items():
    with open("data/items.json") as f:
        item_data = json.load(f)
        retrieved_items = {}
        for item in item_data:
            attributes = {}

            for key, value in item.items():
                if key not in ["id", "name", "description", "value", "long_description", "use"]:
                    attributes[key] = value
            retrieved_items[item["id"]] = Item(
                item["id"],
                item["name"],
                item["description"],
                item["value"],
                item["long_description"],
                item["use"],
                attributes
            )
    return retrieved_items


def load_zones(items):
    with open("data/zones.json") as f:
        zone_data = json.load(f)
        retrieved_zones = {}
        for zone in zone_data:
            retrieved_zones[zone["id"]] = Zone(
                zone["id"],
                zone["name"],
                zone["description"],
                zone["long_description"]
            )

        for zone in zone_data:
            for direction, neighbor_id in zone["neighbors"].items():
                retrieved_zones[zone["id"]].add_neighbor(
                    retrieved_zones[neighbor_id],
                    direction
                )
            if "items" in zone:
                for item_id in zone["items"]:
                    retrieved_zones[zone["id"]].add_item(items[item_id])

    return retrieved_zones


# TODO: define actions as their own functions




def process_command(player, action):
    action = action.lower()

    # movement
    if action == "move" or action == "m":
        direction = input("Which direction would you like to move? ")
        player.move(direction)
    elif action == "west" or action == "w":
        player.move("west")
    elif action == "east" or action == "e":
        player.move("east")
    elif action == "north" or action == "n":
        player.move("north")
    elif action == "south" or action == "s":
        player.move("south")

    # interacting with the environment
    elif action == "look" or action == 'l' or action == 'examine' or action == 'look around':
        print(player.current_zone.look())
        player.looked = True
    elif action == "take" or action == 't' or action == 'pick up' or action == 'grab' or action == 'get':
        if player.current_zone.items:
            item_name = input("What would you like to take? ")
            for item in player.current_zone.items:
                if item.name.lower() == item_name.lower():
                    player.take_item(item)
                    break
            else:
                print("That item is not here.")
    elif action == "use" or action == 'u':
        item_name = input("What would you like to use? ")
        player.use_item_from_inventory(item_name)

    # TODO: add ability to search items like chests

    # other actions
    elif action == "help" or action == '?':
        print_help()
    elif action == "quit" or action == 'q' or action == 'exit':
        return False

    # catch
    else:
        print("I don't understand that command.")

    return True