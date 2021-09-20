# Main classes that everything will inherit from
class Person:
    def __init__(self, name: str, health: int, base_damage: int,
                 weapon: str, ranged_weapon: str, is_good: bool, is_alive: bool):                                        # Key attributes that all 'persons'
        self.__name = name                                                                                               # will have
        self.__max_health = health
        self.__current_health = health
        self.__base_damage = base_damage
        self.__weapon = weapon
        self.__ranged_weapon = ranged_weapon
        self.__is_good = is_good
        self.__is_alive = is_alive
        self.__inventory = []
        self.__money = 0
    def get_name(self) -> str:                                                                                           # Getters & Setters
        return self.__name
    def get_health(self):
        return self.__current_health
    def get_max_health(self):
        return self.__max_health
    def set_health(self, new_health):
        self.__current_health = new_health
    def take_damage(self, damage: int):
        self.__current_health = self.get_health() - damage
    def heal(self, heal_amount):
        if self.get_health() + heal_amount > self.__max_health:
            self.set_health(self.__max_health)
        else:
            self.set_health(self.get_health() + heal_amount)
        print(f"You have been healed up to {self.get_health()}")
    def get_damage(self):
        return self.__base_damage
    def get_weapon(self):
        return self.__weapon
    def new_weapon(self, new_weapon):
        print(f"Are you sure you want to change your {self.get_weapon()} for a {new_weapon}?")
        decision = input("Type 1 to change or 2 to keep.")
        checker = True
        while checker:
            if decision == 1:
                self.__weapon = new_weapon
                print(f"You now have the {new_weapon}!")
                checker = False
            elif decision == 2:
                print(f"You have decided to keep your {self.get_weapon()}")
                checker = False
            else:
                print("Please enter only 1 or 2")
    def is_good(self):
        return self.__is_good
    def change_of_heart(self):
        if self.is_good():
            self.__is_good = False
        else:
            self.__is_good = True
    def get_is_alive(self):
        return self.__is_alive
    def kill_off(self):
        if not self.__is_alive:
            print("They're already dead!")
        else:
            self.__is_alive = False
    def resurrect(self):
        if self.__is_alive:
            print("They're already alive!")
        else:
            self.__is_alive = True
    def get_inventory(self):
        return self.__inventory
    def add_to_inventory(self, item):
        self.__inventory.append(item)
    def get_balance(self):
        return self.__money
    def change_balance(self, change):
        self.__money += change
class Animal:
    def __init__(self, name: int, health: int, damage: int):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__is_good = None
    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def set_health(self, new_health):
        self.__health = new_health
    def get_damage(self):
        return self.__damage
    def get_good(self):
        return self.__is_good
    def set_allignment(self, good: bool):
        if good:
            self.__is_good = True
        else:
            self.__is_good = False

class Items:
    def __init__(self, name:str, cost: int, category: str):
        self.__name = name
        self.__cost = cost
        self.__category = category
    def get_name(self):
        return self.__name
    def get_category(self):
        return self.__category