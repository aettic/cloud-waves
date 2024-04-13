import json
from player import Player
from zone import Zone
from items.item import Item
import game_utils

if __name__ == "__main__":

    # greet the player
    player = game_utils.welcome()
    print(f"Hello {player.name}, let's begin.")
    game_utils.story()

    # load content
    items = game_utils.load_items()
    zones = game_utils.load_zones(items)

    # set starting zone
    player.current_zone = zones[1]

    # game loop
    while True:
        game_utils.print_instructions(player)
        if not game_utils.process_command(player, input("What would you like to do? ")):
            game_utils.goodbye(player)
            break
