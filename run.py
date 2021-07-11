def you_die(why):
    print(f"{why}")
    exit()


def start_adventure():
    
    door_picked = (input("Which door do you choose? Left or right?").lower())
    if door_picked == "left":
        print("You picked the door on the left")
        left_door()
    elif door_picked == "right":
        print("You picked the door on the right")
        right_door()
    else:
        print (input("Please pick left or right"))

def left_door():
    print("The door handle clunks as you turn it.\nIt opens.\n You can see two narrow green eyes looking at you. ")
    print("Do you flee or fight?")
    next_move = input("> ").lower()
    if "flee" in next_move:
        print("You chose to flee.\n You are back in the damp, dark room.\nYou forgot to close the door.\n The two green eyes follow you and become a large scaly ...")
        you_die("A ferocious large green dragon barbecues you")
    elif "fight" in next_move:
        print("You chose to fight")
    else:
        print("If you don't choose you die!")
        you_die("A ferocious large green dragon barbecues you")
        
def right_door():
    wooden_box = ["axe", "knife", "crossbow and arrows", "shotgun" ]
    print("The door bangs open.\nInside the room there is a wooden box with the lid closed.\n You can hear footsteps approaching.\n")
    # ask player what to do
    action = input("What do you do? >")
    # list of keywords to see user input
    if action.lower() in ['box', 'open', 'lid']:
        print("Quick! Let's see if there's a weapon in the box")
    else:
        print("Let's see who's coming ")



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