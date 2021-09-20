from Animal import *
import MAsterClass as MC

class Wolf(Animal):

    def __init__(self, name: str, colour: str, type: str, health: int, damage: int):
        self.name = name
        self.colour = colour
        self.type = type
        self.health = health  # Health points/number of lives
        self.damage = damage  # Attack power

    def declare(self):
        print("Grrrrrr. I will kill you and your measly friends before you can harm my master.\n Grrrrrrr")


# Create an instance
my_wolf = Wolf("Thunder", "black", "Wild", 100, 100)

print(my_wolf.name)
print(my_wolf.colour)
print(my_wolf.type)
print(my_wolf.health)
print(my_wolf.damage)

my_wolf.declare()
