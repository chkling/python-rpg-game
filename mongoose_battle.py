

from animal_classes import Mongoose, Python

# from gooseClass import pythonAttack, Mongoose
# from jwalden2019 import Python, mongoose_play_dead, mongoose_claw_attack, eat_berries
# from python_rpg import victory_message, defeat_message


mongoose = Mongoose("Mongoose", 150)
python = Python("Python", 150)
berry_amount = 3

def fight_result ():
    if mongoose.health <= 0:
        print("The Mongoose has been defeated...")
        exit()
    elif python.health <= 0:
        print("The Python has been killed!!!")
        exit()

def main_menu():
    fight_result()
    message = int(input("""
    What would you like to do?\n\n
    1. Claw at the Python
    2. Play dead...
    3. Eat a berry
    4. View Mongoose' health
    5. Run away\n
    ********************
    """))
    while message != "q":   
        if message == 1:
            mongoose.mongoose_claw_attack(mongoose, python)  
            python.pythonAttack(mongoose, python)         
            main_menu()
        elif message == 2:
            mongoose.mongoose_play_dead(mongoose, python) 
            main_menu()
        elif message == 3:
            mongoose.eat_berries()
            main_menu()
        elif message == 4:   
            mongoose.view_stats()
            main_menu()
        elif message == 5:
            mongoose.run_away()
        else:
            return print("Please input a valid option.")
            main_menu()


welcome_image = print("""
           /^\/^\\
         _|__|  O|
\/     /~     \_/ \\
 \____|__________/  \\
        \_______      \\
                `\     \                 \\
                  |     |                  \\
                 /      /                    \\
                /     /                       \\
              /      /                         \ \\
             /     /                            \  \\
           /     /             _----_            \   \\
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
""")
print("You are a Mongoose. A wild Python has appeared!")

main_menu()

