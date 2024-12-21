#15
a = int(input("Enter the number of students in the first class: "))
b = int(input("Enter the number of students in the second class: "))
c = int(input("Enter the number of students in the third class: "))
desks = (a + 1) // 2 + (b + 1) // 2 +(c + 1) //2
print(f"Minimun desks needed: {desks}")