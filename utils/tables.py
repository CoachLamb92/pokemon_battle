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

types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]

type_chart = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],            #normal
        [1, 0.5, 0.5, 2, 1, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],        #fire
        [1, 2, 0.5, 0.5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],          #water
        [1, 0.5, 2, 0.5, 1, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1],  #grass
        [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],            #electric
        [1, 0.5, 0.5, 2, 1, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],            #ice
        [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5],            #fighting
        [1, 1, 1, 2, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2],            #poison
        [1, 2, 1, 0.5, 2, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1],            #ground
        [1, 1, 1, 2, 0.5, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1],            #flying
        [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],            #psychic
        [1, 0.5, 1, 2, 1, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5],            #bug
        [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],            #rock
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1],            #ghost
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0],            #dragon
        [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5],            #dark
        [1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2],            #steel
        [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]             #fairy
        ]

test_moves = [
[10, 'scratch', 'PLACEHOLDER', 'normal', 35, 100, 40, 'physical'],
[33, 'tackle', 'PLACEHOLDER', 'normal', 35, 100, 40, 'physical'],
[39, 'tail-whip', 'PLACEHOLDER', 'normal', 30, 100, -1, 'status'],
[45, 'growl', 'PLACEHOLDER', 'normal', 40, 100, -1, 'status'],
[52, 'ember', 'PLACEHOLDER', 'fire', 25, 100, 40, 'special'],
[145, 'bubble', 'PLACEHOLDER', 'water', 30, 100, 40, 'special']]