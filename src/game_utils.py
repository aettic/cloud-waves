import json
from player import Player
from items.item import Item
from zone import Zone
import textwrap

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


def print_handler(string):
    print(textwrap.fill(string, width=100))
    return True


def print_instructions(player):
    print_handler("\n")
    if player.current_zone not in player.visited_zones:
        player.visited_zones.add(player.current_zone)
        print_handler(f"You are in the {player.current_zone.name}, {player.current_zone.description}.")
    else:
        print_handler(f"You are in the {player.current_zone.name}.")

    if player.looked:
        if player.current_zone.items:
            print_handler("You see the following items:")
            for item in player.current_zone.items:
                print_handler(f"  {item.name}")

    player.looked = False




def goodbye(player):
    print(f"Goodbye, {player.name}!")
    print(f"Your score was {player.score}.")


def quit_game():
    return False


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


def process_command(player, action):
    action = action.lower().split()

    commands = {
        player.move: ["move", "m", "go"],
        player.look: ["look", "l", "examine"],
        player.take_item: ["take", "t", "grab", "get"],
        player.use_item_from_inventory: ["use", "u", "activate"],
        print_help: ["help", "?"],
        quit_game: ["quit", "q", "exit"],
        player.open_inventory: ["inventory", "i"]
    }

    command_found = False

    for command, options in commands.items():
        if action[0] in options:
            if len(action) > 1 and action[0] in ["move", "m", "go", "take", "t", "grab", "get", "use", "u"]:
                command(action[1])
            else:
                process = command()
                if not process:
                    return False
            command_found = True
            break

    if not command_found:
        print("I do not understand that command.")

    # TODO: add ability to search items like chests

    return True
