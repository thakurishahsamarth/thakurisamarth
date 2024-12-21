weight = float(input("Enter the weight of the package in kg: "))
is_urgent = input("Is the delivery urgent? (yes/no): ").lower() #Direct method yei == 'yes'
if weight < 5:
    cost = 5
elif 5 <= weight <= 20:
    cost = 10
else:
    cost = 20
if is_urgent== 'yes' :  
    cost += 5
print(f"Delivery cost: ${cost}\n")