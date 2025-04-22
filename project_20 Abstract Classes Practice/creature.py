from abc import ABC, abstractmethod
import random

class Creature(ABC):

    @abstractmethod
    def attack(self):
        print("The creature has attacked!")

    @abstractmethod
    def roar(self):
        raise NotImplementedError("This error must be implemented!")


class Dragon(Creature):
    def __init__(self, name):
        self.name = name

        def attack(self):
            print(f"The dragon has attacked!")

        def roar(self):
            print("AOOOOOOOOOOOOOR!")


class Gargoyle(Creature):
    def __init__(self):

        def attack(self):
            print("The gargoyle has attacked!")

        def roar(self):
            print("EWABUNGABUNGABUNGA")


class Troll(Creature):
    def __init__(self):

        def attack(self):
            print("The Troll has attacked!")

        def roar(self):
            print("TTTTTTTTTTTROOOOL")




    
        


    