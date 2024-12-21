age = int(input("Enter your age: "))
gender = input("Select your gender(Male,Female): ")
day = int(input("Enter your number of days: "))
if 18 <= age <30:
    if 18 <= age < 30:
        wage_per_day = 700 if gender == 'M' else 750
elif 30 <= age <= 40:
    wage_per_day = 800 if gender == 'M' else 850
    total_wages = wage_per_day * day
    print(f"Total wages for {day} days: ${total_wages}")
else:
    print("Invalid input. Please enter valid numbers.")




