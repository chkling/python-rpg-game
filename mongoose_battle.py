



from gooseClass import pythonAttack, Mongoose
from jwalden2019 import Python, mongoose_bite_attack, mongoose_claw_attack
from python_rpg import main_menu, victory_message, defeat_message, view_stats


char1 = Mongoose("Crazy Ricky", 150)
char2 = Python("Big Johnson", 150)

def run_away():
    print("You run away!")
    exit()

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
    while message != "q":        
        if message == 1:
            mongoose_bite_attack(char1, char2)            
            main_menu()
        elif message == 2:
            mongoose_claw_attack(char1, char2)
            main_menu()
        elif message == 3:
            eat_berry(char1)
            main_menu()
        elif message == 4:   
            view_stats(char1)
            main_menu()
        elif message == 5:
            run_away()
        else:
            return print("Please input a valid option.")
            main_menu()



print("You are a Mongoose. A wild Python has appeared!")
main_menu()
