## CLASS TEMPLATES ##
class Python:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage_play_dead(self):
        self.health -= 50

    def take_damage_claw(self):
        self.health -= 20

    # def damage(self):
    #     self.health -= 15
    
    def pythonAttack(self, char1, char2):
        char1.damage(40)
        print(f"{char2.name} chokes {char1.name} his health is at {char1.health} now")

class Mongoose:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def damage(self, damage):
        self.health -= damage

    def eat_berries(self):
        print(f"{self.name} eats a handful of berries")
        self.health += 25
        print(f"{self.name} gains 25 health.")
        print(f"{self.name} has {self.health} remaining.")
    
    def mongoose_play_dead(self, char1, char2):
        print(f"{char1.name} attacks {char2.name}")
        char2.take_damage_play_dead()
        print(f"{char2.name} takes 50 damage.")
        print(f"{char2.name} has {char2.health} health points left.")

    def mongoose_claw_attack(self, char1, char2):
        print(f"{char1.name} attacks {char2.name}")
        char2.take_damage_claw()
        print(f"{char2.name} takes 20 damage.")
        print(f"{char2.name} has {char2.health} remaining.")

    def view_stats(self):
        print(f"{self.name} has {self.health} health.")

    def run_away(self):
        print(f"{self.name} runs away!")
        exit()

# class Mongoose:
#     def __init__(self, name, health):
#         self.name = name   
#         self.health = health
#     def take_damage_python_bite(self):
#         self.health -= 20
#     def eat_berries(self):
#         self.health += 25

# char1 = Mongoose("Crazy Ricky", 150)
# char2 = Python("Big Johnson", 150)

## CHARACTER FUNCTIONS ##






# def eat_berries():
#     print(f"{char1.name} eats a handful of berries")
#     char1.eat_berries()
#     print(f"{char1.name} gains 25 health.")
#     print(f"{char1.name} has {char1.health} remaining.")


# def main_menu():
#     message = """
#     Welcome to Mongoose Versus Python!
    
#     You're just a laid back mongoose vibing in the wilderness...
#     When suddenly, from the shadows of the marshland, a python springs its trap!
    
#     Press 1 to Play Dead then Attack (damage equals 20)
#     Press 2 to Do Claw Swipe (damage equals 10)
#     Press 3 to Eat Berries (boost health by 25)
#     Press q to End Game
# """
    # print(message)
    # option = input("Select an option: ")
    # while option != "q":
    #     if option == "1":
    #         mongoose_play_dead(char1, char2)
    #         main_menu()
    #     elif option == "2":
    #         mongoose_claw_attack(char1, char2)
    #         main_menu()
    #     elif option == "3":
    #         eat_berries()
    #         main_menu()
    #     elif option == "q":
    #         sys_quit()



