class Dog:

    animal_kind = "canine" # Class variable

    def bark(self):
        print(self.animal_kind)
        return "woof!"

print(Dog.animal_kind)
print(Dog().bark())

Dog.animal_kind = "dolphin"

fido = Dog()   # Instatiation
lassie = Dog() # Instatiation

fido.animal_kind = "Big Dog"

print(fido.animal_kind)
print(lassie.animal_kind)
