class Mongoose:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    # def damage(self):
    #   self.hp -= 15

    def damage(self):
      self.health -= 25

    def berry(self):
      self.health += 40
    
    def view_stats(self):
      print(f"{self.name} has {self.health} health.")

# character1 = Mongoose("Goose", 75)
# character2 = Mongoose("Thon", 130)

def pythonAttack(char1, char2):
  char1.damage()
  print(f"{char2.name} chokes {char1.name} his health is at {char1.health} now")

# pythonAttack(character1, character2)

# print("George uses bite on Goose")
# goose.damage()
# print(f"Goose has {goose.hp} left!")
# print("George uses choke on Goose ")
# goose.damage()
# print(f"Goose has {goose.hp} left!")
# goose.berry()
# print(f"Goose has eaten a berry his health is now {goose.hp}")
