#13. A company decided to give bonus of 5% to employee if his/her year of 
#    service is more than 5years. Ask user for their salary and year of service 
#    and print the net bonus amount.
 
time = int(input("Enter your time period of service: "))
salary = int( input("Enter your salary: "))
if time > 5:
    bonus = salary * 0.05
    print(f"Your bonus is {bonus}")
else:
    print("Your time of service is not enough")