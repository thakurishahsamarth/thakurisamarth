#10. Accept the grades from the user and display the grade according to the 
#    following criteria: 
#    Below 25 --D 
#    25 to 45  -- C 
#    45 to 50 -- B 
#    50 to 60 --B+ 
#    60 to 80 -- A 
#    Above 80 -- A+

grade = int(input("Enter your grade: "))
if grade < 25:
    print("Your grade is: D")
elif 25 <= grade <= 45:
    print("Your grade is: C")
elif 45 <= grade <= 50:
    print("Your grade is: B")
elif 50 <= grade <= 60:
    print("Your grade is: B+")
elif 60 <= grade <= 80:
    print("Your grade is: A")
else:
    print("Your grade is: A+")