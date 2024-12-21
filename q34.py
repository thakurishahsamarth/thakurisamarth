print("Welcome to the Jungle Adventure")
choice1 = input("Do you want to go 'left' or 'right'? ").lower()
if choice1 == "right":
    print("Game Over\n")
elif choice1 == "left":
    choice2 = input("Do you want to 'climb a tree' or 'explore the cave'? ").lower()
    if choice2 == "climb a tree":
        print("Game Over\n")
    elif choice2 == "explore the cave":
        choice3 = input("Choose between 'bear', 'tiger', or 'snake': ").lower()
        if choice3 in ["bear", "tiger"]:
            print("Game Over\n")
        elif choice3 == "snake":
            print("You Win\n")