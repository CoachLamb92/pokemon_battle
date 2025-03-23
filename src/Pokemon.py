import json
from utils.tables import nature_list, type_chart, types
from random import randrange
import math
# from Move import Move

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
        self._current_health = self.get_stats()["hp"]
        
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
    
    def get_current_health(self):
        return self._current_health
    
    def restore_current_health(self):
        self._current_health = self.get_stats()["hp"]

    def take_damage(self, damage):
        self._current_health = max(0, self._current_health-damage)

    def move_success_check(self, move):
        roll = randrange(1, 101)
        if roll <= move.get_accuracy():
            print(f"{self.get_pokemon_name()} used {move.get_move_name()}!")
            self.execute_move(move)
        else:
            print("The move failed/missed!")

    def execute_move(self, move, opponent_pokemon):
        if move.get_category() != "status":
            if move.get_power() > 0:
                self.deal_damage(move, opponent_pokemon)
            else:
                print("This move does 0 or less damage")
        else:
            print("This is a non-damaging move")

    def deal_damage(self, move, pokemon):
        damage = self.calculate_damage(move, pokemon)
        pokemon.take_damage(damage)

    def calculate_damage(self, move, pokemon):
        if move.get_category() == "physical":
            # print(self.get_stats()["attack"], "bulb attack1")
            # print(pokemon.get_stats()["defense"], " squirt def1")
            cat_ratio = self.get_stats()["attack"]/pokemon.get_stats()["defense"]
            # print(cat_ratio, "cat_ratio")
        elif move.get_category() == "special":
            cat_ratio = self.get_stats()["special-attack"]/pokemon.get_stats()["special-defense"]
        else:
            print("This should only return for a status move")
            return 0
        
        base_calc = round((((((2*self.get_level()))//5)+2)*move.get_power()*(cat_ratio))/50)
        # print(base_calc, "base_calc")
        # next brackets include Burn, Screen, Targets, Weather, FlashFire
        tier_2_calc = (base_calc * 1 * 1 * 1 * 1 * 1 + 2)//1
        # final bracket includes Stockpile, Critical, DoubleDmg, Charge, HelpingHand, STAB, Type1, Type2, random
        # critical = calculate_crit_chance()
        critical = 2 if randrange(1, 25) == 1 else 1
        stab = 1.5 if move.get_type() in self.get_types() else 1
        # make this a function?
        attacking_index = types.index(move.get_type())
        type_multiplier = 1
        for type in pokemon.get_types():
            defending_index = types.index(type)
            type_multiplier *= type_chart[attacking_index][defending_index]
        if type_multiplier == 0:
            print(f"It didn't affect the {pokemon.get_pokemon_name()}!")
            return 0
        elif type_multiplier == 0.5 or type_multiplier == 0.25:
            output_text = "It wasn't very effective!"
        elif type_multiplier == 2 or type_multiplier == 4:
            output_text = "It was super-effective!"
        else:
            output_text = ""
        final_calc = (tier_2_calc * 1 * critical * 1 * 1 * 1 * stab * type_multiplier * randrange(85, 100))//100
        if output_text: print(output_text)
        # print(final_calc)
        return max(final_calc, 1)
    
    def is_fainted(self):
        if self.get_current_health() == 0:
            return True
        return False