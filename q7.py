#  7. Write a program to accept the cost price of a bike qnd display the road tax 
#  to be paid according to the following criteria: 

cost_price = int(input("Enter the cost price of a bike: "))
if cost_price > 100000:
    tax = cost_price * 0.15
    print(f"Your tax is {tax}")
elif cost_price > 50000 and cost_price <= 100000:
    tax = cost_price * 0.10
    print(f"Your tax is {tax}")
elif cost_price <= 50000:
    tax = cost_price * 0.05
    print(f"Your tax is {tax}")
else:
    print("Invailed cost")
