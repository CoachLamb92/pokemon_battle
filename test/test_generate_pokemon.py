from utils.generate_pokemon import generate_pokemon

def test_basic_pokemon_generation():
    # Arrange
    input_pokemon = "bulbasaur"
    input_level = 5
    expected_name = "bulbasaur"
    expected_level = 5
    expected_types = ["grass", "poison"]
    expected_moves = set(['33', '45'])
    # Act
    result = generate_pokemon(input_pokemon, input_level)
    # Assert
    assert result.get_pokemon_name() == expected_name
    assert result.get_level() == expected_level
    assert result.get_types() == expected_types
    assert set(result.get_moves()) == expected_moves

def test_basic_pokemon_generation_including_set_moves():
    # Arrange
    input_pokemon = "charmander"
    input_level = 5
    expected_name = "charmander"
    expected_level = 5
    expected_types = ["fire"]
    expected_moves = set(['14', '15'])
    # Act
    result = generate_pokemon(input_pokemon, input_level, ['14', '15'])
    # Assert
    assert result.get_pokemon_name() == expected_name
    assert result.get_level() == expected_level
    assert result.get_types() == expected_types
    assert set(result.get_moves()) == expected_moves

def test_basic_pokemon_generation_higher_level():
    # Arrange
    input_pokemon = "squirtle"
    input_level = 8
    expected_name = "squirtle"
    expected_level = 8
    expected_types = ["water"]
    expected_moves = set(['39', '266', '33', '145'])
    # Act
    result = generate_pokemon(input_pokemon, input_level)
    # Assert
    assert result.get_pokemon_name() == expected_name
    assert result.get_level() == expected_level
    assert result.get_types() == expected_types
    assert set(result.get_moves()) == expected_moves
