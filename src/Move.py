# from db.connection import connect_to_db, close_connection # <- when db added
from utils.tables import test_moves # <delete when DB connected
class Move:

    def __init__(self, id):
        # db = connect_to_db() <Post DB conn
        # result = db.run("SELECT * FROM moves WHERE move_id = 10")[0] <Post DB conn
        # close_connection(db) <Post DB conn
        # _, name, text, type, pp, acc, power, category = result
        for move in test_moves:
            if move[0] == id:
                self._move_name = move[1]
                self._description = move[2]
                self._type = move[3]
                self._total_powerpoints = move[4]
                self._accuracy = move[5]
                self._power = move[6]
                self._category = move[7]
                break
        self._current_powerpoints = self.get_total_powerpoints()

    def get_move_name(self):
        return self._move_name
    
    def get_description(self):
        return self._description
    
    def get_type(self):
        return self._type
    
    def get_total_powerpoints(self):
        return self._total_powerpoints
    
    def get_current_powerpoints(self):
        return self._current_powerpoints
    
    def set_current_powerpoints(self, amount):
        self._current_powerpoints = amount

    def reduce_pp_using_move(self):
        if self.can_use_move:
            amount = self.get_current_powerpoints() - 1
            self.set_current_powerpoints(amount)
        else:
            print("This move has ran out of powerpoints!")

    def restore_powerpoints_fully(self):
        amount = self.get_total_powerpoints()
        self.set_current_powerpoints(amount)

    def get_accuracy(self):
        return self._accuracy
    
    def get_power(self):
        return self._power
    
    def get_category(self):
        return self._category
    
    def can_use_move(self):
        return bool(self.get_current_powerpoints())
