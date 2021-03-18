# mongoose vs python
# main menu - attack, play dead, eat berry, run away

def main_menu():
    message = """
    A wild Python has appeared!\n
    What would you like to do?\n\n
    1. Bite the Python
    2. Play dead...
    3. Eat a berry
    3. View Mongoose stats
    4. Run away\n
    """
    return print(message)













option = ""
while option != "5":
    main_menu()
    if option == "1":
        print("You bite the python for x damage.")
        print("The python bites you for x damage.")
    elif option == "2":
        print("You play dead...")
        print("The python approaches to inspect you.")
        print("You surprise attack with your bite and claws for x damage!")
    elif option == "3":
        print("You eat a berry and regain x HP!")
    elif option == "4":
        pass
    elif option == "5":
        pass
    else:
        print("Please input a valid option.")
main_menu()