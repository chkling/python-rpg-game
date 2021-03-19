from animal_classes import Mongoose, Python

mongoose = Mongoose("Mongoose", 200)
python = Python("Python", 300)
berry_amount = 3

def fight_result ():
    if mongoose.health <= 0:
        print("The Mongoose has been defeated...")
        exit()
    elif python.health <= 0:
        print("The Python has been killed!!!")

def fight_result ():
    if mongoose.health <= 0:

        print("""
                 
                                                  
                         (,,(,                   
                      (,'     `/                           
                  ,  ,'  ,--.  `,                           
                   `{R, {    \  :                                       
                     C,,'    /  /                                        
                     |;;    /  ,' ,--.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'  \n
        The Mongoose dies in battle!""")
        exit()
    elif python.health <= 0:
        print("""
                                                         _...---.._
                                                     _.'`       -_  `.
                                                 .-'`                  \\
                                              .-`                     O
                                           _-`                       __  \\
                                       .-'`                  . ' .   \ `;/
                                   _.-`                    /       `._`/
                           _...--'`                        \_
                        .'`                         -         `'--.._
                     . `                           \                  `-.
                    .                `              `-..__. ... - -.._`-
                   '.                `  '''---- -''`                  `-.`.
                 .` -                '`.  `-.
              .-` .` '             .`'.__ ;
          _.-` .-`   '            .
      _.-`  .-`       '         .`
(`''-'' _.-`          '        .'
 `'---''            .`       .`
                 .'     . '`
                .    .-`
              .`   ,`
             '   .'
           '   .`
          '  .`
          `  '.    
          `.___;\n
        The Python perishes in battle!!!""")

        exit()

def main_menu():
    fight_result()
    message = int(input("""
    What would you like to do?\n\n
    1. You swipe your claw across python's body. 
    2. Pretend to die then surprise attack. 
    3. Eat berries. (boost health)
    4. View Mongoose's health
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
            print(f"The Python launches a surprise attack dealing 100 damage!!!")
            mongoose.damage(100)
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
print("You are a mongoose, just vibin in the wilderness, when suddenly a python appears!")

main_menu()

