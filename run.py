def start_adventure():
    #print("You wake up in a dark, damp room.")
    #print("You don't know how you got there.")
    print("As your eyes adjust you can make out two doors, one on the left and one on the right.")
    door_picked = (input("Which door do you choose? Left or right?").lower())
    if door_picked == "left":
        print("You picked the door on the left")
    elif door_picked == "right":
        print("You picked the door on the right")
    else:
        print (input("Please pick left or right"))



# def main():
    
#     #print(input("What's your name? >"))
#     player_name = input("What's your name? >")
#     print(f"Hi {player_name}!")
#     player_character = input("What character would you like to be? E.g. knight, assassin >")
#     print(f"Your name is {player_name.upper()}. You are a {player_character}! Cool!")
start_adventure()

# if __name__ == "__main__":
#     main()