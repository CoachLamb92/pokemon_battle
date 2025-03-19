from src.Pokemon import Pokemon
import json
import math
from random import randrange
from pprint import pprint

def generate_pokemon(pokemon, level, moves=None):
    # gets relevant data file
    filepath = f"small_data/{pokemon}.json"
    
    # loads data into a dict
    with open(filepath, "r") as f:
        pokemon_dict = json.load(f)

    # randomly generates IVs
    IVs = {"hp": randrange(0, 32),
             "attack": randrange(0, 32),
             "defense": randrange(0, 32),
             "special-attack": randrange(0, 32),
             "special-defense": randrange(0, 32),
             "speed": randrange(0, 32)}
    
    # sets EVs to 0 for generating pokemon
    EV = 0
    # lists each nature by its name, increased stat, decreased stat
    nature_list = [("adamant", "attack", "special-attack"),
               ("bashful", "special-attack", "special-attack"),
               ("bold", "defense", "attack"),
               ("brave", "attack", "speed"),
               ("calm", "special-defense", "attack"),
               ("careful", "special-defense", "special-attack"),
               ("docile", "defense", "defense"),
               ("gentle", "special-defense", "defense"),
               ("hardy", "attack", "attack"),
               ("hasty", "speed", "defense"),
               ("impish", "defense", "special-attack"),
               ("jolly", "speed", "special-attack"),
               ("lax", "defense", "special-defense"),
               ("lonely", "attack", "defense"),
               ("mild", "special-attack", "defense"),
               ("modest", "special-attack", "attack"),
               ("naive", "speed", "special-defense"),
               ("naughty", "attack", "special-defense"),
               ("quiet", "special-attack", "speed"),
               ("quirky", "special-defense", "special-defense"),
               ("rash", "special-attack", "special-defense"),
               ("relaxed", "defense", "speed"),
               ("sassy", "special-defense", "speed"),
               ("serious", "speed", "speed"),
               ("timid", "speed", "attack")
               ]
    # randomly picks a nature
    nature = nature_list[randrange(0, 25)]
    # generates the total stats of the pokemon (excluding EVs)
    stats = {"hp": math.floor(0.01 * (2 * pokemon_dict["hp"] + IVs["hp"] + math.floor(0.25 * EV)) * level) + level + 10,
             "attack": (math.floor(0.01 * (2 * pokemon_dict["attack"] + IVs["attack"] + math.floor(0.25 * EV)) * level) + 5),
             "defense": (math.floor(0.01 * (2 * pokemon_dict["defense"] + IVs["defense"] + math.floor(0.25 * EV)) * level) + 5),
             "special-attack": (math.floor(0.01 * (2 * pokemon_dict["special-attack"] + IVs["special-attack"] + math.floor(0.25 * EV)) * level) + 5),
             "special-defense": (math.floor(0.01 * (2 * pokemon_dict["special-defense"] + IVs["special-defense"] + math.floor(0.25 * EV)) * level) + 5),
             "speed": (math.floor(0.01 * (2 * pokemon_dict["speed"] + IVs["speed"] + math.floor(0.25 * EV)) * level) + 5)
             }
    # applies nature buff/debuff if the nature is non_neutral
    if nature[1] != nature[2]:
        stats[nature[1]] = math.floor(stats[nature[1]] * 1.1)
        stats[nature[2]] = math.floor(stats[nature[2]] * 0.9)

    if moves == None:
        moves = []
        potential_moves = [move['move_id'] for move in pokemon_dict["moves"] if move["move_learn_method"] == "level-up" and move['level_learned_at'] <= level]
        while potential_moves and len(moves) < 4:
            random_move_index = randrange(0, len(potential_moves))
            moves.append(potential_moves.pop(random_move_index))

    output_pokemon = Pokemon(pokemon, level, moves, stats)
    return output_pokemon
