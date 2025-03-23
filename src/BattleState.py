from src import Pokemon
from src import Trainer

class BattleState:

    def __inti__(self, player, opponent):
        self._player = player
        self._current_player_pokemon = "" # "" = player.leading_pokemon() (Create trainer class)
        self._opponent = opponent
        if isinstance(opponent, Pokemon):
            self._current_opponent_pokemon = opponent
        elif isinstance(opponent, Trainer):
            self._current_opponent_pokemon = "" # "" = opponent.leading_pokemon()
