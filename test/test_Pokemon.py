from src.Pokemon import Pokemon
from src.Move import Move
from unittest.mock import patch

class Test_Pokemon_Attributes:
    def test_set_pokemon_attributes(self):
        # Arrange
        input_poke = 'bulbasaur'
        input_level = 5
        expected_name = 'bulbasaur'
        expected_level = 5
        expected_types = ["grass", "poison"]
        expected_moves = ['33', '45']
        expected_ability = 34
        # Act
        result = Pokemon(input_poke, input_level)
        # Assert
        assert result._pokemon_name == expected_name
        assert result._level == expected_level
        assert result._types == expected_types
        assert set(result._moves) == set(expected_moves)
        assert result._ability == expected_ability

    def test_set_pokemon_attributes_again(self):
        # Arrange
        input_poke = 'charmander'
        input_level = 15
        expected_name = 'charmander'
        expected_level = 15
        expected_types = ["fire"]
        expected_moves = ['10', '45', '52', '232']
        expected_ability = 94
        # Act
        result = Pokemon(input_poke, input_level)
        # Assert
        assert result._pokemon_name == expected_name
        assert result._level == expected_level
        assert result._types == expected_types
        assert set(result._moves) == set(expected_moves)
        assert result._ability == expected_ability

class Test_Pokemon_Methods:
    def test_retrieve_base_stats_returns_correctly(self):
        # Arrange
        input_poke = "squirtle"
        input_level = 7
        expected_stats = {"hp": 44,
                          "attack": 48,
                          "defense": 65,
                          "special-attack": 50,
                          "special-defense": 64,
                          "speed": 43
                          }
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        result = dummy_pokemon.retrieve_base_stats()
        # Assert
        assert result == expected_stats

    def test_update_stats_with_nature_returns_correctly(self):
        # Arrange
        input_poke = "squirtle"
        input_level = 7
        input_stats = {"hp": 100,
                       "attack": 100,
                       "defense": 100,
                       "special-attack": 100,
                       "special-defense": 100,
                       "speed": 100
                        }
        input_nature = ("brave", "attack", "speed")
        expected_stats = {"hp": 100,
                          "attack": 110,
                          "defense": 100,
                          "special-attack": 100,
                          "special-defense": 100,
                          "speed": 90
                          }
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon._stats = input_stats
        dummy_pokemon._nature = input_nature
        dummy_pokemon.update_stats_with_nature()
        result = dummy_pokemon._stats 
        # Assert
        assert result == expected_stats

    def test_initialise_move_list_returns_correctly_when_no_moves_passed_in(self):
        # Arrange
        input_poke = "squirtle"
        input_level = 7
        expected_moves = ['33', '39', '145', '266']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        result = dummy_pokemon._moves 
        # Assert
        assert set(result) == set(expected_moves)

    def test_initialise_move_list_returns_correctly_when_moves_passed_in(self):
        # Arrange
        input_poke = "squirtle"
        input_level = 7
        input_moves = ['1']
        expected_moves = ['1']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level, input_moves)
        result = dummy_pokemon._moves 
        # Assert
        assert set(result) == set(expected_moves)

        # Arrange
        input_poke = "bulbasaur"
        input_level = 77
        input_moves = ['1', '13', '100']
        expected_moves = ['1', '13', '100']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level, input_moves)
        result = dummy_pokemon._moves 
        # Assert
        assert set(result) == set(expected_moves)

    def test_get_pokemon_name_returns_correctly(self):
        # Arrange
        input_poke = "charmander"
        input_level = 17
        expected_name = "charmander"
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        result = dummy_pokemon.get_pokemon_name()
        # Assert
        assert result == expected_name

    def test_set_pokemon_name_sets_correctly(self):
        # Arrange
        input_poke = "charmander"
        input_level = 17
        expected_name = "Bill"
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon.set_pokemon_name("Bill")
        result = dummy_pokemon.get_pokemon_name()
        # Assert
        assert result == expected_name

    def test_get_level_returns_correctly(self):
        # Arrange
        input_poke = "bulbasaur"
        input_level = 43
        expected_level = 43
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        result = dummy_pokemon.get_level()
        # Assert
        assert result == expected_level

    def test_set_level_sets_correctly(self):
        # Arrange
        input_poke = "squirtle"
        input_level = 4
        expected_level = 3
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon.set_level(3)
        result = dummy_pokemon.get_level()
        # Assert
        assert result == expected_level

    def test_get_moves_returns_correctly_when_no_moves_passed_in(self):
        # Arrange
        input_poke = "bulbasaur"
        input_level = 5
        expected_moves = ['45', '33']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        result = dummy_pokemon.get_moves()
        # Assert
        assert set(result) == set(expected_moves)

    def test_get_moves_returns_correctly_when_moves_passed_in(self):
        # Arrange
        input_poke = "charmander"
        input_level = 23
        input_moves = ['1', '2', '3', '4']
        expected_moves = ['1', '2', '3', '4']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level, input_moves)
        result = dummy_pokemon.get_moves()
        # Assert
        assert result == expected_moves

    def test_set_moves_sets_correctly_no_overwrite(self):
        # Arrange
        input_poke = "squirtle"
        input_level = 5
        expected_moves = ['33', '39', '266','267']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon.set_moves('267')
        result = dummy_pokemon.get_moves()
        # Assert
        assert set(result) == set(expected_moves)

    def test_set_moves_sets_correctly_overwrite(self):
        # Arrange
        input_poke = "squirtle"
        input_level = 8
        expected_moves = ['267', '39', '145','266']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon.set_moves('267', '33')
        result = dummy_pokemon.get_moves()
        # Assert
        assert set(result) == set(expected_moves)

    def test_get_stats_returns_correctly(self):
        # Arrange
        input_poke = "bulbasaur"
        input_level = 5
        input_stats = {"hp": 10,
                       "attack": 20,
                       "defense": 30,
                       "special-attack": 40,
                       "special-defense": 50,
                       "speed": 60
                        }
        expected_stats = {"hp": 10,
                          "attack": 20,
                          "defense": 30,
                          "special-attack": 40,
                          "special-defense": 50,
                          "speed": 60
                          }
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon._stats = input_stats
        result = dummy_pokemon.get_stats()
        # Assert
        assert result == expected_stats

    def test_set_stats_sets_correctly(self):
        # Arrange
        input_poke = "charmander"
        input_level = 5
        input_stats = {"hp": 15,
                       "attack": 25,
                       "defense": 35,
                       "special-attack": 45,
                       "special-defense": 55,
                       "speed": 65
                        }
        expected_stats = {"hp": 15,
                          "attack": 25,
                          "defense": 35,
                          "special-attack": 45,
                          "special-defense": 55,
                          "speed": 65
                          }
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon.set_stats(input_stats)
        result = dummy_pokemon.get_stats()
        # Assert
        assert result == expected_stats

    def test_get_types_returns_correctly(self):
        # Arrange
        input_poke = "charmander"
        input_level = 5
        expected_types = ['fire']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        result = dummy_pokemon.get_types()
        # Assert
        assert result == expected_types

    def test_set_types_sets_correctly(self):
        # Arrange
        input_poke = "charmander"
        input_level = 5
        expected_types = ['water']
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon.set_types(['water'])
        result = dummy_pokemon.get_types()
        # Assert
        assert result == expected_types

    def test_get_current_health_returns_correctly(self):
        # Arrange
        input_poke = "charmander"
        input_level = 5
        expected = 50
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        dummy_pokemon._current_health = 50
        result = dummy_pokemon.get_current_health()
        # Assert
        assert expected == result

class Test_Pokemon_Further_Methods:
    def test_restore_current_health_returns_correctly(self):
        # Arrange
        input_poke = "squirtle"
        input_level = 5
        # Act
        dummy_pokemon = Pokemon(input_poke, input_level)
        initial_health = dummy_pokemon.get_current_health()
        dummy_pokemon._current_health = 3
        reduced_health = dummy_pokemon.get_current_health()
        dummy_pokemon.restore_current_health()
        result = dummy_pokemon.get_current_health()
        # Assert
        assert initial_health == result
        assert reduced_health == 3

    def test_take_damage_works_correctly(self):
        # Arrange
        input_poke = "bulbasaur"
        # Act
        dummy_pokemon = Pokemon(input_poke, 5)
        initial_health = dummy_pokemon.get_current_health()
        dummy_pokemon.take_damage(1)
        result = dummy_pokemon.get_current_health()
        # Assert
        assert result == initial_health - 1

        # Arrange
        input_poke = "squirtle"
        # Act
        dummy_pokemon = Pokemon(input_poke, 5)
        initial_health = dummy_pokemon.get_current_health()
        dummy_pokemon.take_damage(5)
        result = dummy_pokemon.get_current_health()
        # Assert
        assert result == initial_health - 5

    def test_move_success_check_returns_correctly_for_zero_accuracy_move(self):
        # Arrange
        expected = "The move failed/missed!"
        # Act
        dummy_pokemon = Pokemon("charmander", 5)
        dummy_move = Move(147)   # nobble, 1% accuracy
        result = dummy_pokemon.move_success_check(dummy_move)
        # Assert
        assert result == None

    # def test_move_success_check_returns_correctly_for_full_accuracy_move(self):
    #     # Arrange
    #     # Act
    #     dummy_pokemon = Pokemon("charmander", 5)
    #     dummy_move = Move(10)   # scratch, 100% accuracy   
    #     result = dummy_pokemon.move_success_check(dummy_move)
    #     # Assert
    #     assert result == None

    def test_execute_move_prints_correctly_for_status_move(self):
        # Arrange
        expected = "This is a non-damaging move"
        attacking_pokemon = Pokemon("bulbasaur", 5)
        defending_pokemon = Pokemon("squirtle", 5)
        dummy_move = Move(45)   # growl, status move
        # Act
        result = attacking_pokemon.execute_move(dummy_move, defending_pokemon)
        # Assert
        # assert result == expected

    def test_execute_move_prints_correctly_for_non_damaging_move(self):
        # Arrange
        expected = "This move does 0 or less damage"
        attacking_pokemon = Pokemon("bulbasaur", 5)
        defending_pokemon = Pokemon("squirtle", 5)
        dummy_move = Move(148)   # splash, zero damage move
        # Act
        result = attacking_pokemon.execute_move(dummy_move, defending_pokemon)
        # Assert
        # assert result == expected

    # def test_execute_move_calls_function_correctly(self):
    #     # Arrange
        # attacking_pokemon = Pokemon("bulbasaur", 5)
        # defending_pokemon = Pokemon("squirtle", 5)
        # dummy_move = Move(10)   # scratch, damaging move
    #     # Act
        # result = attacking_pokemon.execute_move(dummy_move, defending_pokemon)
    #     # Assert

    # def test_deal_damage_returns_correctly(self):
        # Arrange
        # attacking_pokemon = Pokemon("bulbasaur", 5)
        # defending_pokemon = Pokemon("squirtle", 5)
        # dummy_move = Move(10)   # scratch, damaging move

    # def test calculate_damage_returns_correctly(self):
        # Arrange

        # Act

        # Assert