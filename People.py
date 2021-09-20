import MasterClass as MC


class GoodGuy(MC.Person):
    def __init__(self, name: str, health: int, base_damage: int, weapon: str, ranged_weapon="", is_good=True,
                 is_alive=True):
        super().__init__(name, health, base_damage, weapon, ranged_weapon, is_good, is_alive)


class BadGuy(MC.Person):
    def __init__(self, name: str, health: int, base_damage: int, weapon: str, ranged_weapon="", is_good=False,
                 is_alive=True):
        super().__init__(name, health, base_damage, weapon, ranged_weapon, is_good, is_alive)

    def evil_cackle(self):
        print("Mwahahahahahahaaaa")


class NeutralGuy(MC.Person):
    def __init__(self, name: str, health: int):
        super().__init__(name, health, base_damage=0, weapon="", ranged_weapon="", is_good=True, is_alive=True)


class Doctor(NeutralGuy):
    def __init__(self, name: str, health: int, heal_power: int):
        super().__init__(name=name, health=health)
        self.__heal_power = heal_power

    def get_heal_power(self):
        return self.__heal_power


class Shopkeeper(NeutralGuy):
    def __init__(self, name: str, health: int, inventory: list):
        super().__init__(name=name, health=health)
        self.__inventory = inventory


blacksmith = Shopkeeper("gary", 5000000000000000000, sword)

class Wizard(NeutralGuy):
    def __init__(self, name:str, health:int):
        super().__init(name=name, health = health)

enemy_list = []
friend_list = []
dead_list = []
doctor_list = []

list_of_good_names = ["Jimmy", "Pieface", "Pinky", "Robin", "Bluebird", "Snapper", "Dan", "Doiby", "Fatman",
                      "Pete Ross", "Sandy", "Squire", "Bucky", "Rick Jones", "Toro", "Bert", "Chippy"]
list_of_bad_names = ["Wiggins", "LeFou", "Horace", "Jasper", "Flotsam", "Jetsam", "Gaston", "Kronk", "Mr. Smee",
                     "Shenzl", "Banzai", "Ed", "Edd", "Eddy", "Annie", "Harry Warden", "Billy", "Freddy", "Jason"]
list_of_sidekicks = ["Perilous Paula", "Not-Nice Nish", "Masterful Martin"]
list_of_doctor_names = ["Capaldi", "Smith", "Tennant", "Eccleston", "Baker", "Hartnell", "Davison", "Pertwee", "Baker",
                        "Grant", "Atkinson"]


