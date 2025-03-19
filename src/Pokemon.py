import json

class Pokemon:
    def __init__(self, pokemon, level, moves, stats):
        self._pokemon_name = pokemon
        self._level = level
        self._moves = moves
        self._stats = stats
        filepath = f"small_data/{pokemon}.json"
        with open(filepath, "r") as f:
            self._types = json.load(f)["types"]

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
      
