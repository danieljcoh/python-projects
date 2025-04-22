import random
from creature import *

class Dungeon:
    def __init__(self):
        self.number_of_levels = random.randint(1, 10)
        self.current_level = 1

        def next_level(self):
            if self.current_level < self.number_of_levels:
                self.current_level += 1
            else:
                print("Game over!")
        
        def create_creature(self):
            random_num = random.randint(1, 3)
            if random_num == 1:
                creature = Dragon()
            elif random_num == 2:
                creature = Gargoyle()
            else:
                creature = Troll()

            return creature

