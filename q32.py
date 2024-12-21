weather = input("Enter the weather (sunny/rainy): ").lower()
if weather == "sunny":
    print("Recommended activities: Hiking, Picnic\n")
elif weather == "rainy":
    has_raincoat = input("Do you have a raincoat or umbrella? (yes/no): ").lower() == "yes"
    if has_raincoat:
        print("Suggested: Visit a nearby mall or museum\n")
    else:
        print("Suggested: Stay home and watch movies\n")
else:
    print("Invalid weather input\n")