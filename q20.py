num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("choose a operator (+,-,*,/): ")
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invaild operator"
print(f"Your Answer is: {result}")
       

    


