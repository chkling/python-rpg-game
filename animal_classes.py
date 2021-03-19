## CLASS TEMPLATES ##
class Python:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage_play_dead(self):
        self.health -= 50

    def take_damage_claw(self):
        self.health -= 20

    def pythonAttack(self, char1, char2):
        char1.damage(40)
        print(f"{char2.name} squeezes {char1.name}, his health diminishes to {char1.health}.")

class Mongoose:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def damage(self, damage):
        self.health -= damage

    
    def eat_berries(self):
        while self.health < 100:
            print(f"{self.name} eats a plump berry.")
            self.health += 60
            print(f"{self.name} gains 60 health.")
            print(f"{self.name} has {self.health} remaining.")
            return
        else:
            return print(f"{self.name} is too full to eat berries!")
    
    def mongoose_play_dead(self, char1, char2):
        print(f"{char1.name} lulls {char2.name} into thinking it's dead.. then attacks!")
        char2.take_damage_play_dead()
        print(f"{char2.name} takes 50 damage.")
        print(f"{char2.name} has {char2.health} health points remaining.")

    def mongoose_claw_attack(self, char1, char2):
        print(f"{char1.name} swipes at {char2.name} with it's claw!")
        char2.take_damage_claw()
        print(f"{char2.name} takes 20 damage.")
        print(f"{char2.name} has {char2.health} health points remaining.")

    def view_stats(self):
        print(f"{self.name} has {self.health} health points remaining.")

    def run_away(self):
        print(f"{self.name} thinks about running away.. but that would be so cowardly, wouldn't it?")
        return