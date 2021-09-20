from Animal import *
import MasterClass as MC

class Troll(Animal):

    def __init__(self, name: str, colour: str, type: str, health: int, damage: int):
        self.name = name
        self.colour = colour
        self.type = type
        self.health = health  # Health points/number of lives
        self.damage = damage  # Attack power

    def declare(self):
        print("*Sniffs*\n I smell some yummy food.\n Looks Like i'll be in for a treat.\n You human and your friends "
              "welcome to hell!!\n Mwahahahahaha")



# Create an instance
my_troll = Troll("Talos", "green", "Wild", 100, 100)

print(my_troll.name)
print(my_troll.colour)
print(my_troll.type)
print(my_troll.health)
print(my_troll.damage)

my_troll.declare()
