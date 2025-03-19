from utils.tables import type_chart, types

def test_single_type_check():
    # Arrange
    attacking = 'fire'
    defending = 'normal'
    expected_multiplier = 1
    # Act
    attacking_index = types.index(attacking)
    defending_index = types.index(defending)
    result = type_chart[attacking_index][defending_index]
    # Assert
    assert result == expected_multiplier

    # Arrange
    attacking = 'normal'
    defending = 'steel'
    expected_multiplier = 0.5
    # Act
    attacking_index = types.index(attacking)
    defending_index = types.index(defending)
    result = type_chart[attacking_index][defending_index]
    # Assert
    assert result == expected_multiplier

    # Arrange
    attacking = 'fighting'
    defending = 'normal'
    expected_multiplier = 2
    # Act
    attacking_index = types.index(attacking)
    defending_index = types.index(defending)
    result = type_chart[attacking_index][defending_index]
    # Assert
    assert result == expected_multiplier

def test_double_type_check():
    # Arrange
    attacking = 'fire'
    defending = ['bug', 'grass']
    expected_multiplier = 4
    # Act
    attacking_index = types.index(attacking)
    result = 1
    for type in defending:
        defending_index = types.index(type)
        result *= type_chart[attacking_index][defending_index]
    # Assert
    assert result == expected_multiplier

    # Arrange
    attacking = 'fairy'
    defending = ['fire', 'steel']
    expected_multiplier = 0.25
    # Act
    attacking_index = types.index(attacking)
    result = 1
    for type in defending:
        defending_index = types.index(type)
        result *= type_chart[attacking_index][defending_index]
    # Assert
    assert result == expected_multiplier

    # Arrange
    attacking = 'water'
    defending = ['grass', 'fire']
    expected_multiplier = 1
    # Act
    attacking_index = types.index(attacking)
    result = 1
    for type in defending:
        defending_index = types.index(type)
        result *= type_chart[attacking_index][defending_index]
    # Assert
    assert result == expected_multiplier

    # Arrange
    attacking = 'water'
    defending = ['fire']
    expected_multiplier = 2
    # Act
    attacking_index = types.index(attacking)
    result = 1
    for type in defending:
        defending_index = types.index(type)
        result *= type_chart[attacking_index][defending_index]
    # Assert
    assert result == expected_multiplier