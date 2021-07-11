def start_adventure():
    
    door_picked = (input("Which door do you choose? Left or right?").lower())
    if door_picked == "left":
        print("You picked the door on the left")
        left_door()
    elif door_picked == "right":
        print("You picked the door on the right")
    else:
        print (input("Please pick left or right"))

def left_door():
    print("The door handle clunks as you turn it.\nIt opens.\n You can see two narrow green eyes looking at you. ")
    flee_fight = (input("Do you flee or fight?").lower())
    if flee_fight == "flee":
        print("You chose to flee.\n You are back in the damp, dark room")
        start_adventure()
    elif flee_fight == "fight":
        print("You chose to fight")
    else:
        print("If you don't choose you die!")



def main():
    
     
     player_name = input("What's your name? >")
     print(f"Hi {player_name}!")
     player_character = input("What character would you like to be? E.g. knight, assassin >")
     print(f"Your name is {player_name.upper()}. You are a {player_character}! Cool!")
     print("You wake up in a dark, damp room.")
     print("You don't know how you got there.")
     print("As your eyes adjust you can make out two doors, one on the left and one on the right.")

     start_adventure()

if __name__ == "__main__":
     main()