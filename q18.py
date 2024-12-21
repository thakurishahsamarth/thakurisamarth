# 18
monuments = {"Delhi": "Red Fort","Agra": "Taj Mahal","Jaipur": "Jal Mahal"}
city = input("Enter a city (Delhi/Agra/Jaipur): ").capitalize()
if city in monuments:
        print(f"Monument in {city} is {monuments[city]}")
else:
        print("City not found in database")