#14. Write a python program which accepts the radius of circle from user and 
#    compute the area.
import math 
user_input = float(input("Enter the radius: "))
area = math.pi* (user_input)**2
print(f"The area if circle is {area}")

