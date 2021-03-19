

from animal_classes import Mongoose, Python

# from gooseClass import pythonAttack, Mongoose
# from jwalden2019 import Python, mongoose_play_dead, mongoose_claw_attack, eat_berries
# from python_rpg import victory_message, defeat_message


ricky = Mongoose("Crazy Ricky", 150)
joe = Python("Dirty Joe", 150)

def fight_result ():
    if ricky.health <= 0:
        print("The Mongoose has been defeated...")
        exit()
    elif joe.health <= 0:
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
            ricky.mongoose_claw_attack(ricky, joe)  
            joe.pythonAttack(ricky, joe)         
            main_menu()
        elif message == 2:
            ricky.mongoose_play_dead(ricky, joe) 
            main_menu()
        elif message == 3:
            ricky.eat_berries()
            main_menu()
        elif message == 4:   
            ricky.view_stats()
            main_menu()
        elif message == 5:
            ricky.run_away()
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

