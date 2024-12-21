percentage = int(input("Enter your percentage: "))
if percentage < 40:
    print("Failed")
elif 40 <= percentage < 55:
    print("Fair")
elif 55 <= percentage < 65:
    print("Good")
else:
    print("Excellent")
