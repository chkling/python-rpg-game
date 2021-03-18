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

goose = Mongoose("Goose", 75)

def pythonAttack(character1, character2):
  print(f"{character2.name} chokes {character1}")


# print("George uses bite on Goose")
# goose.damage()
# print(f"Goose has {goose.hp} left!")
# print("George uses choke on Goose ")
# goose.damage()
# print(f"Goose has {goose.hp} left!")
# goose.berry()
# print(f"Goose has eaten a berry his health is now {goose.hp}")
