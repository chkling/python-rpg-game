def run_away():
    print("You run away!")
    exit()

def battleOptions():
    print("""
    A wild Python has appeared!
    What would you like to do?
    """)

option = ""
while option != "q":
    main_menu()
     # main_menu()
    if option == 1:
        mongoose_bite_attack()            
    elif option == 2:
        mongoose_claw_attack()
         #play dead attack
    elif option == 3:
         pass
    # call function to eat berry for health
    elif option == 4:   
        view_stats()        
    # view stats function
    elif option == 5:
        run_away()
    else:
        return print("Please input a valid option.")