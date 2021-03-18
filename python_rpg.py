# mongoose vs python
# main menu - attack, play dead, eat berry, run away

def main_menu():
    message = int(input("""
    What would you like to do?\n\n
    1. Bite the Python
    2. Play dead...
    3. Eat a berry
    4. View Mongoose stats
    5. Run away\n
    ********************
    """))
    return print(message)

def victory_message():
    if char2.health == 0:
    print("The Mongoose has slain the Python!!!")

def defeat_message():
    if char1.health == 0:
    print ("The Python defeats the Mongoose...")

def view_stats():
    print(f"The {goose.name} has {goose.attack} and {goose.hp} health.")

# option = ""
# while option != 5:
#     main_menu()
#     if option == 1:
#         pass
#     if option == 2:
#         pass
#     if option == 3:
#         pass
#     if option == 4:
#         pass
#     if option == 5:
#         pass