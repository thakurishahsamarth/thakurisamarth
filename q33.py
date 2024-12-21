print("Welcome to the Haunted House")
choice1 = input("Do you want to go 'upstairs' or 'downstairs'? ").lower()
if choice1 == "downstairs":
    print("Game Over\n")
elif choice1 == "upstairs":
    choice2 = input("Do you want to 'enter the room' or 'stay outside'? ").lower()
    if choice2 == "enter the room":
        print("Game Over\n")
    elif choice2 == "stay outside":
        choice3 = input("Choose between 'ghost', 'vampire', or 'werewolf': ").lower()
        if choice3 in ["ghost", "vampire"]:
            print("Game Over\n")
        elif choice3 == "werewolf":
            print("You Win\n")