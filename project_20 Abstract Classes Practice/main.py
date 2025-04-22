from creature import *
from dungeon import *
import random

d1 = Dungeon()
monsters = [d1.create_creature() for i in range(d1.number_of_levels)]

# add monsters to the list of monsters!
print(monsters)

