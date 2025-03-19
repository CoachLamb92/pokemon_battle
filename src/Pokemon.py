import json
from utils.tables import nature_list
from random import randrange
import math

class Pokemon:
    def __init__(self, pokemon, level, moves=None):
        self._pokemon_name = pokemon
        self._level = level
        self._moves = moves
        self._base_stats = self.retrieve_base_stats()
        self._IVs = {"hp": randrange(0, 32),
             "attack": randrange(0, 32),
             "defense": randrange(0, 32),
             "special-attack": randrange(0, 32),
             "special-defense": randrange(0, 32),
             "speed": randrange(0, 32)}
        self._EVs = {"hp": 0,
             "attack": 0,
             "defense": 0,
             "special-attack": 0,
             "special-defense": 0,
             "speed": 0}
        self._nature = nature_list[randrange(0, 25)]
        self._stats = {"hp": math.floor(0.01 * (2 * self._base_stats["hp"] + self._IVs["hp"] + math.floor(0.25 * self._EVs["hp"])) * level) + level + 10,
             "attack": (math.floor(0.01 * (2 * self._base_stats["attack"] + self._IVs["attack"] + math.floor(0.25 * self._EVs["attack"])) * level) + 5),
             "defense": (math.floor(0.01 * (2 * self._base_stats["defense"] + self._IVs["defense"] + math.floor(0.25 * self._EVs["defense"])) * level) + 5),
             "special-attack": (math.floor(0.01 * (2 * self._base_stats["special-attack"] + self._IVs["special-attack"] + math.floor(0.25 * self._EVs["special-attack"])) * level) + 5),
             "special-defense": (math.floor(0.01 * (2 * self._base_stats["special-defense"] + self._IVs["special-defense"] + math.floor(0.25 * self._EVs["special-defense"])) * level) + 5),
             "speed": (math.floor(0.01 * (2 * self._base_stats["speed"] + self._IVs["speed"] + math.floor(0.25 * self._EVs["speed"])) * level) + 5)
             }
        self.update_stats_with_nature()
        filepath = f"small_data/{self._pokemon_name}.json"
        with open(filepath, "r") as f:
            dictionary = json.load(f)
            self._types = dictionary["types"]
            self._ability = dictionary["abilities"][0]
        self.initialise_move_list()
        
    def retrieve_base_stats(self):
        filepath = f"small_data/{self._pokemon_name}.json"
        with open(filepath, "r") as f:
            pokemon_dict = json.load(f)
        return {"hp": pokemon_dict["hp"],
                "attack": pokemon_dict["attack"],
                "defense": pokemon_dict["defense"],
                "special-attack": pokemon_dict["special-attack"],
                "special-defense": pokemon_dict["special-defense"],
                "speed": pokemon_dict["speed"]
                }

    def update_stats_with_nature(self):
        if self._nature[1] != self._nature[2]:
            self._stats[self._nature[1]] = math.floor(self._stats[self._nature[1]] * 1.1)
            self._stats[self._nature[2]] = math.floor(self._stats[self._nature[2]] * 0.9)

    def initialise_move_list(self):
        if self._moves == None:
            moves = []
            filepath = f"small_data/{self._pokemon_name}.json"
            with open(filepath, "r") as f:
                pokemon_dict = json.load(f)
            potential_moves = [move['move_id'] for move in pokemon_dict["moves"] if move["move_learn_method"] == "level-up" and move['level_learned_at'] <= self._level]
            while potential_moves and len(moves) < 4:
                random_move_index = randrange(0, len(potential_moves))
                moves.append(potential_moves.pop(random_move_index))
            self._moves = moves

    def get_pokemon_name(self): 
        return self._pokemon_name 
      
    def set_pokemon_name(self, new_pkmn_name): 
        self._pokemon_name = new_pkmn_name

    def get_level(self): 
        return self._level
    
    def set_level(self, new_level):
        self._level = new_level

    def get_moves(self): 
        return self._moves
      
    def set_moves(self, new_move, old_move = None):
        if len(self.get_moves()) < 4:
            self._moves.append(new_move)
        else:
            ind = self.get_moves().index(old_move)
            self._moves[ind] = new_move

    def get_stats(self): 
        return self._stats 
      
    def set_stats(self, new_stats): 
        self._stats = new_stats

    def get_types(self): 
        return self._types 
      
    def set_types(self, new_types): 
        self._types = new_types
      
