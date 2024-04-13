# Cloud Waves

## Description

This is a small text-based adventure game set in a fantasy world. In it, the player controls a hero investigating some
mystery. Details to be fleshed out later.  

This game is a spiritual successor to a project called Aetrynos which I built in Python in 2022. Back then, I was still 
pretty new to programming and I didn't know how to structure a project like this. I'm building this project to be more 
organized and to include more features, as well as to be more extensible so it can be used to build other games.

## Running the game

Execute the main.py file in the src directory.
`python3 src/main.py`

## Plans

Below are lists of my plans or goals for this game. The goal is to create an engine first and foremost, which can use 
world files that will include data such as items, zones, characters, and so on. I will include documentation on how to 
format these data files later. The data files are in JSON format, and the engine will be able to read them and create 
the world inside the engine, so it can be played. The game is designed as a single-player experience.

For now, I'm planning to flesh out a single game world to include with the engine. This will feature a story, 
characters, etc. in a fantasy setting. I'll include information on the setting and world in the game-world.md file.

### Must Haves

- [ ] Write a story of some kind
- [ ] Add more locations
- [ ] Add more items
- [ ] Add characters
- [ ] Add puzzles
- [ ] Add combat
- [ ] Add a save system
- [ ] Add an options system
- [ ] Add a settings system
- [x] Add an inventory system
- [ ] Add environmental systems (described below)
- [ ] Add a magic system
- [x] Implement a language parser

### Stretch Goals

- [ ] Add a day/night cycle
- [ ] Add a weather system
- [ ] Add a crafting system
- [ ] Add a leveling system
- [ ] Add a quest system
- [ ] Add a dialogue system
- [ ] Add a shop system
- [ ] Add a skill system
- [ ] Add a stats system
- [ ] Add a journal system
- [ ] Add a map system

## Mechanics

The game will be a text-based adventure game. The player will be able to move around the world, interact with objects,
pickup and use items, talk to characters, and solve puzzles. The game will also include combat, a magic system, and a
save system.

The game uses a basic language parser to interpret the player's input. The player can type commands such as "move north"
to traverse the various zones. Zones can contain items, which the user may interact with.

### List of Possible Actions
- move (m) - move in a specified direction to an adjacent zone
- look (l) - examine the current zone
- take (t) - take an item that is in the current zone
- inventory (i) - view the player's inventory, which provides options for interacting with items
- stats - view the player's stats
- help (?) - view a list of possible commands
- save - save the game
- load - load a saved game
- quit (q) - quit the game

With these basic mechanics, many game worlds can be created, as long as they fit into the basic components of the game 
as described above. However, users can add or change functionality as well. The plan is to include "laws of nature" for 
the game world which will define how the world works, and should be relatively common across all game worlds. 

### Mechanics Systems (Laws of Nature)
- [ ] Time (Day / Night)
- [ ] Temperature
- [ ] Light
- [ ] Weather
- [ ] Fire and Water
- [ ] Magical effects

## License

This project is licensed under CC BY-NC-SA 4.0. See the LICENSE file for more information.