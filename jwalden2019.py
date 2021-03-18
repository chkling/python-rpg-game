## CLASS/CHARACTERS ##
class Python:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def take_damage_bite(self):
        self.health -= 10
    def take_damage_claw(self):
        self.health -= 20

class Mongoose:
    def __init__(self, name, health):
        self.name = name   
        self.health = health
    def take_damage_python_bite(self):
        self.health -= 10


char1 = Mongoose("Crazy Ricky", 150)
char2 = Python("Big Johnson", 150)

def mongoose_bite_attack(char1, char2):
    print(f"{char1.name} attacks {char2.name}")
    char2.take_damage_bite()
    print(f"{char2.name} takes 10 damage.")
    print(f"{char2.name} has {char2.health} health points left.")

def mongoose_claw_attack(char1, char2):
    print(f"{char1.name} attacks {char2.name}")
    char2.take_damage_claw()
    print(f"{char2.name} takes 20 damage.")
    print(f"{char2.name} has {char2.health} health points left.")

# while option != "q":
#     if option == "1":
