a = {1:'january', 2:'february', 3:'march',4:'april',5:'may',6:'may',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
user_input = int(input("Enter a number: "))
if user_input in a:
    result=a[user_input]
    print(result)
else:
    print("the given number is out of range")
