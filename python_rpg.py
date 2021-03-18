# mongoose vs python
# main menu - attack, play dead, eat berry, run away



def victory_message():
    if char2.health == 0:
    print("The Mongoose has slain the Python!!!")

def defeat_message():
    if char1.health == 0:
    print ("The Python defeats the Mongoose...")

def view_stats():
    print(f"The {goose.name} has {goose.attack} and {goose.hp} health.")
