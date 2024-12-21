age = int(input("Enter candidate's age: "))
if age >= 18:
    has_degree = input("Do you have a degree? (yes/no): ").lower()
    if has_degree == "yes":
        experience = float(input("Enter your work experience in years: "))
        if experience > 3:
            print("Highly Eligible\n")
        elif 1 <= experience <= 3:
            print("Eligible\n")
        else:
            print("Under Review\n")
    else:
        print("Not Eligible\n")
else:
    print("Not Eligible\n")