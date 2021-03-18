def run_away():
    print("You run away!")
    exit()

def battleOptions():
    option = int(input("""
    A wild Python has appeared!
    What would you like to do?
    """))
    while option != "q":
        # main_menu()
        if option == 1:
            pass
    # call function to bite python
    # call function to hurt mongoose
        elif option == 2:
            pass
    # call function to play dead, don't call python attack 
        elif option == 3:
            pass
    # call function to eat berry for health
        elif option == 4:   
            pass         
    # view stats function
        elif option == 5:
            run_away()
        else:
            return print("Please input a valid option.")

battleOptions()