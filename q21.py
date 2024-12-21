total = int(input("Enter the total number of days: "))
absent = int(input("Number of days for absent : "))
attended = total - absent
percentage = (attended/total)*100
if percentage < 75:
    print(f"Your attendance percentage is {percentage:.2f}%. You are not allowed to sit in the exam.")
else:
    print(f"Your attendance percentage is {percentage:.2f}%. You are allowed to sit in the exam.")