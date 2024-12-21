#6. WAP which accepts marks of four subjects and display total marks, percentage and grade.
 #  Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –> pass,  less than 40 –> fail 
subject1 = int(input("Enter your marks for subject1: "))
subject2 = int(input("Enter your marks for subject2: "))
subject3 = int(input("Enter your marks for subject3: "))
subject4 = int(input("Enter your marks for subject4: "))

total_marks = subject1 + subject2 + subject3 + subject4
percentage = (total_marks/400)*100
if percentage >= 70:
    grade = "distinction"
elif percentage >= 60 and percentage <= 70:
    grade = "first"
elif percentage >= 40 and percentage <= 60:
    grade = "pass"
else:
    grade = "fail"
print(f"Total Marks: {total_marks}") 
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
