score = float(input("Enter subject score: "))
if score > 90:
    print("Congratulations!\n")
elif 50 <= score <= 90:
    print("Suggest improvement\n")
else:
    print("Advise on retaking the course\n")