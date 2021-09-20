from Animal import *
import MasterClass as MC


class Dog(Animal):

    def __init__(self, name: str, colour: str, type: str, health: int, damage: int):
        self.name = name
        self.colour = colour
        self.type = type
        self.health = health
        self.damage = damage

    def declare(self):
        print(f"Woof. My name is {self.name}.\n I will be your companion throughout your journey")



# Create an instance
my_dog = Dog("Houdini", "golden-brown", "Domestic Pet", 100, 100)

print(my_dog.name)
print(my_dog.colour)
print(my_dog.type)
print(my_dog.health)
print(my_dog.damage)

my_dog.declare()
