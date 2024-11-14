import json
from player import Player
from items.item import Item
from items.container import Container
from zone import Zone
import textwrap


# introductory functions

def welcome():
    name = input("Welcome, what's your name name: ")
    return Player(name)


def story():
    print_handler("You have entered a well-built cabin, in the hopes of finding the ancient amulet.")


# administrative functions

def print_help():
    print_handler("Commands:")
    print_handler("  move (m) - Move to a different zone.")
    print_handler("  look (l) - Look around.")
    print_handler("  take (t) - Take an item.")
    print_handler("  open (o) - Open a container.")
    print_handler("  use (u) - Use an item from your inventory.")
    print_handler("  inventory (i) - Open your inventory.")
    print_handler("  stats - Print your stats.")
    print_handler("  help (?) - Print this list of commands.")
    print_handler("  quit (q) - Quit the game.")
    return True


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
        if player.current_zone.containers:
            print_handler("You see the following containers:")
            for container in player.current_zone.containers:
                print_handler(f"  {container.name}")

    player.looked = False


def goodbye(player):
    print_handler(f"Goodbye, {player.name}!")
    print_handler(f"Your score was {player.score}.")


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


def load_containers(items):
    with open("data/containers.json") as f:
        container_data = json.load(f)
        retrieved_containers = {}
        for container in container_data:

            new_container = Container(
                container["id"],
                container["name"],
                container["description"],
                container["is_open"],
                container["is_locked"],
                container["is_lockable"]
            )

            for item in container["items"]:
                new_container.add_item(items[item])

            retrieved_containers[container["id"]] = new_container

    return retrieved_containers


def load_zones(items, containers):
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

        if "containers" in zone:
            for container_id in zone["containers"]:
                retrieved_zones[zone["id"]].add_container(containers[container_id])

    return retrieved_zones


# processing functions

def process_command(player, action):
    action = action.lower().split()

    commands_with_args = {
        player.move: ["move", "m", "go", "walk", "run"],
        player.take_item: ["take", "t", "grab", "get"],
        player.open_container: ["open", "o"],
        player.search_container: ["search", "s"],
        player.use_item_from_inventory: ["use", "u", "activate"],
    }

    commands_without_args = {
        player.look: ["look", "l"],
        print_help: ["help", "?"],
        quit_game: ["quit", "q", "exit"],
        player.open_inventory: ["inventory", "i"],
        player.get_stats: ["stats"]
    }

    command_found = False

    if len(action) > 1:
        for command, options in commands_with_args.items():
            if action[0] in options:
                command(action[1])
                command_found = True
                break
    else:
        for command, options in commands_without_args.items():
            if action[0] in options:
                process = command()
                if not process:
                    return False
                command_found = True
                break

    if not command_found:
        print_handler("I do not understand that command.")

    # TODO: add ability to search items like chests

    return True
