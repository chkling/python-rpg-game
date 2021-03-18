# mongoose vs python
# main menu - attack, play dead, eat berry, run away

def main_menu():
    message = """
    What would you like to do?\n\n
    1. Bite the Python
    2. Play dead...
    3. Eat a berry
    3. View Mongoose stats
    4. Run away\n
    ********************
    """
    return print(message)


def victory_message():
    print("The Mongoose has slain the Python!!!")

def defeat_message():
    print ("The Python defeats the Mongoose...")

def view_stats():
    print(f"The {goose.name} has {goose.attack} and {goose.health} health.")
