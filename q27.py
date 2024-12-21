num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"The greater number is {num1}\n")
elif num1 < num2:
    print(f"The greater number is {num2}\n")
else:
    if num1 > 0:
        print("Numbers are equal and positive\n")
    elif num1 < 0:
        print("Numbers are equal and negative\n")
    else:
        print("Numbers are equal and zero\n")