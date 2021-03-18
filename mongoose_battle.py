from gooseClass import pythonAttack
from gooseClass import Mongoose
from jwalden2019 import Python
from jwalden2019 import Mongoose
from jwalden2019 import mongoose_bite_attack
from jwalden2019 import mongoose_claw_attack
# from python-rpg.py import main_menu
# from python-rpg.py import victory_message
# from python-rpg.py import defeat_message
# from python-rpg.py import view_stats

def run_away():
    print("You run away!")
    exit()

def battleOptions():
    option = int(input("""
    A wild Python has appeared!
    What would you like to do?
    """))
    while option != "q":
        main_menu()
        if option == 1:
            mongoose_bite_attack()            
            main_menu()
        elif option == 2:
            mongoose_playdead_attack()
            main_menu()
        elif option == 3:
            eat_berry()
            main_menu()
        elif option == 4:   
            view_stats()
            main_menu()
        elif option == 5:
            run_away()
        else:
            return print("Please input a valid option.")

battleOptions()