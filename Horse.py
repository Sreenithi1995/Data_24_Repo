from Animal import *
import MasterClass as MC

class Horse(Animal):

    def __init__(self, name: str, colour: str, type: str, health: int, damage: int):
        self.name = name
        self.colour = colour
        self.type = type
        self.health = health
        self.damage = damage


    def declare(self):
        print(f"Yo man, what's up? I'm {self.name}.\n I'll be accompanying you and Houdini in your quest to defeat the "
              f"dreaded Dastardly Danny")


# Create an instance
my_horse = Horse("Falcon", "brown", "Domestic", 100, 100)

print(my_horse.name)
print(my_horse.colour)
print(my_horse.type)
print(my_horse.health)
print(my_horse.damage)

my_horse.declare()
