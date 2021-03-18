class Mongoose:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    # def damage(self):
    #   self.hp -= 15

    def damage(self):
      self.hp -= 25

    def berry(self):
      self.hp += 40

character1 = Mongoose("Goose", 75)
character2 = Mongoose("Thon", 130)

def pythonAttack(goose, thon):
  goose.damage()
  print(f"{character2.name} chokes {character1.name} his health is at {character1.hp} now")

pythonAttack(character1, character2)

# print("George uses bite on Goose")
# goose.damage()
# print(f"Goose has {goose.hp} left!")
# print("George uses choke on Goose ")
# goose.damage()
# print(f"Goose has {goose.hp} left!")
# goose.berry()
# print(f"Goose has eaten a berry his health is now {goose.hp}")
