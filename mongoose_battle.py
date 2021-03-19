from animal_classes import Mongoose, Python


mongoose = Mongoose("Manny Mongoose", 200)
python = Python("Peter Python", 300)


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
        Manny the mongoose dies in battle!""")
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
        Peter the Python perishes in battle!!!""")
        exit()

def main_menu():
    fight_result()
    message = int(input("""
    What would you like to do?\n\n
    1. Claw attack
    2. Play dead 
    3. Eat a berry
    4. View health
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
            print(f"While you were checking on yourself, Peter the python launches a surprise attack dealing 100 damage!!!")
            mongoose.damage(100)
            mongoose.view_stats()
            main_menu()
        elif message == 5:
            mongoose.run_away()
            main_menu()
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
print("You are Manny the mongoose, just vibin in the wilderness.. when suddenly Peter the python appears!")

main_menu()

