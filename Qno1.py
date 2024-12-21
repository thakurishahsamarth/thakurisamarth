#1. Write a Python Program to Swap Two Variables

a = 10 
b = 20

a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)


#  2. Create a Python program that starts by greeting the user with a message 
#     "Welcome to Treasure Land". Then, prompt the user to choose a direction, 
#     either "left" or "right". If the user chooses "right", print "Game Over". If the user 
#     chooses "left", ask whether they want to "swim" or "wait". If they choose 
#     "swim", print "Game Over". If they choose to "wait", ask them to select a color: 
#     "red", "blue", or "yellow". If the user picks "blue" or "red", print "Game Over". If 
#     they select "yellow", print "You Win".

game = input("Welcome to Treasure Land\nchoose direction:-\n1.left\n2.right\nchoice: ")
if game == "right":
    print("Game Over")
elif game == "left":
    user = int(input("You want to: swim\n wait\nchoice: "))
    if user == 1:
        print("Game Over")
    elif user == 2:
        user_2=input("Select a color:\nred\nblue\nyellow\nchoice: ")
        if user_2 == "blue" or user_2 == "red":
            print("Game Over")
        elif user_2 == "yellow":
            print("You Win") 
        else:
            print("Invalid choice")
    else:
            print("Invalid choice")
else:
            print("Invalid choice")





#4.  For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative 
#    and print ‘zero’ if it is 0


x = int(input("Enter a number: "))
if x > 0:
     print(f"{x} is a positive number")
elif x < 0:
     print(f"{x} is a negative number")
else:
     print(f"{x} is zero")









