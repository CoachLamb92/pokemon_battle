from src.Move import Move

test_moves = [
[10, 'scratch', 'PLACEHOLDER', 'normal', 35, 100, 40, 'physical'],
[33, 'tackle', 'PLACEHOLDER', 'normal', 35, 100, 40, 'physical'],
[39, 'tail-whip', 'PLACEHOLDER', 'normal', 30, 100, -1, 'status'],
[45, 'growl', 'PLACEHOLDER', 'normal', 40, 100, -1, 'status'],
[52, 'ember', 'PLACEHOLDER', 'fire', 25, 100, 40, 'special'],
[145, 'bubble', 'PLACEHOLDER', 'water', 30, 100, 40, 'special']]

class Test_Move_Attributes:
    def test_move_initialises_correctly(self):
        # Arrange
        expected = test_moves[0]    # 'scratch' row
        # Act
        result = Move(10)
        # Assert
        assert expected[1] == result._move_name
        assert expected[2] == result._description
        assert expected[3] == result._type
        assert expected[4] == result._total_powerpoints
        assert expected[4] == result._current_powerpoints
        assert expected[5] == result._accuracy
        assert expected[6] == result._power
        assert expected[7] == result._category

class Test_Move_Methods:
    def test_getters_work_correctly(self):
        # Arrange
        expected = test_moves[4]    # 'ember' row
        # Act
        result = Move(52)
        # Assert
        assert expected[1] == result.get_move_name()
        assert expected[2] == result.get_description()
        assert expected[3] == result.get_type()
        assert expected[4] == result.get_total_powerpoints()
        assert expected[4] == result.get_current_powerpoints()
        assert expected[5] == result.get_accuracy()
        assert expected[6] == result.get_power()
        assert expected[7] == result.get_category()

    def test_set_current_powerpoints_works_correctly(self):
        # Arrange
        expected = test_moves[5]    # 'bubble' row
        expected_initial_pp = expected[4]
        expected_altered_pp = 17
        # Act
        result = Move(145)
        result_initial_pp = result.get_current_powerpoints()
        result.set_current_powerpoints(17)
        result_altered_pp = result.get_current_powerpoints()
        # Assert
        assert expected_initial_pp == result_initial_pp
        assert expected_altered_pp == result_altered_pp

    def test_reduce_pp_using_move_works_correctly(self):
        # Arrange
        expected = test_moves[1]    # 'tackle' row
        expected_initial_pp = expected[4]
        expected_reduced_pp = 34
        # Act
        result = Move(33)
        result_initial_pp = result.get_current_powerpoints()
        result.reduce_pp_using_move()
        result_reduced_pp = result.get_current_powerpoints()
        # Assert
        assert expected_initial_pp == result_initial_pp
        assert expected_reduced_pp == result_reduced_pp

    def test_restore_powerpoints_fully_works_correctly(self):
        # Arrange
        expected = test_moves[2]    # 'tail-whip' row
        expected_initial_pp = expected[4]
        expected_intermediate_pp = 3
        expected_restored_pp = 30
        # Act
        result = Move(39)
        result_initial_pp = result.get_current_powerpoints()
        result.set_current_powerpoints(3)
        result_intermediate_pp = result.get_current_powerpoints()
        result.restore_powerpoints_fully()
        result_restored_pp = result.get_current_powerpoints()
        # Assert
        assert expected_initial_pp == result_initial_pp
        assert expected_intermediate_pp == result_intermediate_pp
        assert expected_restored_pp == result_restored_pp

    def test_can_use_move_returns_True_correctly(self):
        # Arrange
        expected = True
        # Act
        result = Move(10)
        # Assert
        assert expected == result.can_use_move()

        # Arrange
        expected = True
        # Act
        result = Move(10)
        result.set_current_powerpoints(1)
        # Assert
        assert expected == result.can_use_move()

        # Arrange
        expected = True
        # Act
        result = Move(10)
        result.reduce_pp_using_move()
        # Assert
        assert expected == result.can_use_move()

    def test_can_use_move_returns_False_correctly(self):
        # Arrange
        expected = False
        # Act
        result = Move(10)
        result.set_current_powerpoints(0)
        # Assert
        assert expected == result.can_use_move()