from Animal import *


class Centaur(Animal):

    def __init__(self, name: str, colour: str, type: str, health: int, damage: int):
        self.name = name
        self.colour = colour
        self.type = type
        self.health = health  # Health points/number of lives
        self.damage = damage  # Attack power

    def declare(self):
        print(f"Greetings young warrior and co. I am {self.name}.\n I am half horse and half man.\n I am the wizard's assistant. "
              f"The wizard has eagerly been awaiting your arrival (player's name).\n Please follow me")


# Create an instance
my_centaur = Centaur("Orion", "tan", "Magical Creature", 1000, 200)

print(my_centaur.name)
print(my_centaur.colour)
print(my_centaur.type)
print(my_centaur.health)
print(my_centaur.damage)

my_centaur.declare()
