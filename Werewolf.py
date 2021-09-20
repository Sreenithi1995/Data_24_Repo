from Animal import *
import MasterClass as MC

class Werewolf(Animal):

    def __init__(self, name: str, colour: str, type: str, health: int, damage: int):
        self.name = name
        self.colour = colour
        self.type = type
        self.health = health
        self.damage = damage

    def declare(self):
        print("ROOOAAARRR!!\n Who dares enter my den?\n You will now die the most gruesome death in the history of "
              "gruesome "
              "deaths.\n Prepare to die!!")



# Create an instance
my_werewolf = Werewolf("Greyback", "black with red stripes", "Wild", 100, 100)

print(my_werewolf.name)
print(my_werewolf.colour)
print(my_werewolf.type)
print(my_werewolf.health)
print(my_werewolf.damage)

my_werewolf.declare()
