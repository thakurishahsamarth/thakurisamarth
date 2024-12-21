#11. A company decided to give bonus to employee according to following 
#  criteria: 
 #   Time period of service     Bonus 
 #  More than 10 years            10% 
 # >=6 and <=10                  8%    
 # Less than 6 years             5%  

time = int(input("Enter your time period of service: "))
salary = int( input("Enter your salary: "))
if time > 10:
    bonus = salary * 0.10
    print(f"Your bonus is {bonus}")
elif 6 <= time <= 10:
    bonus = salary * 0.08
    print(f"Your bonus is {bonus}")
else:
    bonus = salary * 0.05
    print(f"Your bonus is {bonus}")
                    

