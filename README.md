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
- [ ] Add key / lock system
- [ ] Add combat
- [ ] Add resting
- [ ] Add a save system
- [ ] Add an options system
- [ ] Add a settings system
- [x] Add an inventory system
- [ ] Add handling for different kinds of items 
- [ ] Add environmental systems (described below)
- [ ] Add a magic system
- [x] Implement a language parser
- [x] Implement a print handler (game_utils)

### Stretch Goals

- [ ] Add a time system
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
- [ ] Light
- [ ] Weather
- [ ] Keys and locks
- [ ] Temperature
- [ ] Fire and water
- [ ] Magical effects

#### Time
The game will have a day/night cycle. This will affect the light level in the game, which will affect the player's 
ability to see. The player will have to use a light source in dark areas. It will also affect the behavior of some 
creatures, and the availability of some characters.  

The world runs on ticks. Each tick represents 5 minutes of in-game time. Each action that the player takes will advance 
the game by a certain number of ticks. The player can rest to advance time more quickly.  

#### Light
The game will have a light system. The player will need to use a light source in dark areas. The player will be able to 
find and use torches, lanterns, and other light sources. The player will also be able to create light sources using 
magic or other means.  

For instance, the player can light a match which will provide light in the immediate area, but only for a short time. 
A torch lasts longer than a match, and perhaps provides more light. A lantern lasts indefinitely, but is heavier and 
requires fuel.  

#### Weather
The game will have a weather system. The weather will affect the player's ability to move around or see the world, and 
will affect the behavior of some creatures. The player may need to dress appropriately for the weather. Weather will 
also be random, and will change gradually over time. Most weather will be fair, but it may become windy or even stormy.
This may be implemented through the game world's data files as well (for example, if the game takes place in the summer
it makes sense to have rain and thunderstorms but it doesn't make sense to have a blizzard).

#### Keys and Locks
The game will have a key and lock system. The player will need to find keys to unlock doors, chests, and other objects.
The player may also be able to create "keys" using magic or other means. The player will also be able to pick locks.
Some locks may be more difficult to pick than others.

#### Temperature
This is relative to local environments and objects, not necessarily the temperature of the world. For example, a player 
may need to heat up a metal object to bend it, or cool it down to harden it.

#### Fire and Water
Naturally, fire will also affect both the temperature and light system, but more importantly, it can burn things. Water
can put out fires, but it can also be used to soak things or to water plants. For example, a player may need to water a
plant to make it grow, or to soak a piece of paper to reveal a hidden message.

#### Magical Effects
The tough one... Since magical effects can vary wildly, this will be represented mostly by descriptions of the effects. 
However, some magical effects may play into other mechanical systems - for instance, the player may be able to make a 
magical light source that doesn't require fuel, or a fireball which burns something. The player might have magic spells
to use in combat, or even to solve puzzles. Perhaps a powerful spell could turn the day to night, or vice versa. Each 
magical effect will need to be handled on a case-by-case basis, so they will be a part of the game world data files. 
However, basic concepts of how magic works will be baked into the game engine itself (such as consuming mana, activating
a spell or artifact, etc).



## License

This project is licensed under CC BY-NC-SA 4.0. See the LICENSE file for more information.  